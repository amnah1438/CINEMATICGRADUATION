import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import GraduationSettings, GraduateMessage


# ═══ DISPLAY ═══
def display(request):
    settings = GraduationSettings.objects.first()
    messages = GraduateMessage.objects.filter(is_active=True)
    return render(request, 'board/display.html', {
        'settings': settings,
        'messages': messages,
    })


# ═══ PARENT FORM ═══
def form_view(request):
    settings = GraduationSettings.objects.first()
    error = None
    if request.method == 'POST':
        student = request.POST.get('student_name', '').strip()
        parent  = request.POST.get('parent_name',  '').strip()
        msg     = request.POST.get('message',       '').strip()
        if student and parent and msg:
            GraduateMessage.objects.create(
                student_name=student,
                parent_name=parent,
                message=msg,
            )
            return redirect('success')
        else:
            error = "يرجى ملء جميع الحقول"
    return render(request, 'board/form.html', {'settings': settings, 'error': error})


def success(request):
    return render(request, 'board/success.html')


# ═══ ADMIN PANEL ═══
def _panel_authed(request):
    return request.session.get('panel_authed') is True

def panel_view(request):
    settings = GraduationSettings.objects.first()
    if request.method == 'POST' and 'password' in request.POST:
        pwd = request.POST.get('password', '')
        correct = settings.panel_password if settings else '1446'
        if pwd == correct:
            request.session['panel_authed'] = True
            return redirect('panel')
        return render(request, 'board/panel.html', {'auth': False, 'error': True, 'settings': settings})
    if not _panel_authed(request):
        return render(request, 'board/panel.html', {'auth': False, 'error': False, 'settings': settings})
    messages = GraduateMessage.objects.all().order_by('-created_at')
    return render(request, 'board/panel.html', {'auth': True, 'settings': settings, 'messages': messages})

def panel_logout(request):
    request.session.pop('panel_authed', None)
    return redirect('panel')


# ═══ API: SETTINGS ═══
@csrf_exempt
def api_settings(request):
    if not _panel_authed(request):
        return JsonResponse({'error': 'unauthorized'}, status=403)
    settings, _ = GraduationSettings.objects.get_or_create(pk=1)
    if request.method == 'POST':
        data = json.loads(request.body)
        for field in ['school_name','batch','ticker_text','card_speed','theme','font','custom_primary','custom_accent']:
            if field in data:
                setattr(settings, field, data[field])
        settings.save()
        return JsonResponse({'ok': True})
    return JsonResponse({
        'school_name':    settings.school_name,
        'batch':          settings.batch,
        'ticker_text':    settings.ticker_text,
        'card_speed':     settings.card_speed,
        'theme':          settings.theme,
        'font':           settings.font,
        'custom_primary': settings.custom_primary,
        'custom_accent':  settings.custom_accent,
    })


# ═══ API: PASSWORD ═══
@csrf_exempt
def api_change_password(request):
    if not _panel_authed(request):
        return JsonResponse({'error': 'unauthorized'}, status=403)
    data = json.loads(request.body)
    settings, _ = GraduationSettings.objects.get_or_create(pk=1)
    if data.get('old') != settings.panel_password:
        return JsonResponse({'error': 'wrong'}, status=400)
    settings.panel_password = data.get('new', '1446')
    settings.save()
    return JsonResponse({'ok': True})


# ═══ API: MESSAGES ═══
def api_messages(request):
    if not _panel_authed(request):
        return JsonResponse({'error': 'unauthorized'}, status=403)
    msgs = GraduateMessage.objects.all().order_by('-created_at')
    return JsonResponse({'messages': [
        {'id': m.id, 'studentName': m.student_name, 'parentName': m.parent_name,
         'message': m.message, 'active': m.is_active, 'createdAt': m.created_at.isoformat()}
        for m in msgs
    ]})

@csrf_exempt
def api_message_toggle(request, msg_id):
    if not _panel_authed(request):
        return JsonResponse({'error': 'unauthorized'}, status=403)
    try:
        m = GraduateMessage.objects.get(pk=msg_id)
        m.is_active = not m.is_active
        m.save()
        return JsonResponse({'ok': True, 'active': m.is_active})
    except GraduateMessage.DoesNotExist:
        return JsonResponse({'error': 'not found'}, status=404)

@csrf_exempt
def api_message_delete(request, msg_id):
    if not _panel_authed(request):
        return JsonResponse({'error': 'unauthorized'}, status=403)
    GraduateMessage.objects.filter(pk=msg_id).delete()
    return JsonResponse({'ok': True})

@csrf_exempt
def api_message_delete_all(request):
    if not _panel_authed(request):
        return JsonResponse({'error': 'unauthorized'}, status=403)
    GraduateMessage.objects.all().delete()
    return JsonResponse({'ok': True})
