from django.shortcuts import render, redirect
from .models import GraduationSettings, GraduateMessage


def display(request):
    settings = GraduationSettings.objects.first()
    messages = GraduateMessage.objects.filter(is_active=True)
    return render(request, 'board/display.html', {
        'settings': settings,
        'messages': messages,
    })


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

    return render(request, 'board/form.html', {
        'settings': settings,
        'error': error,
    })


def success(request):
    return render(request, 'board/success.html')
