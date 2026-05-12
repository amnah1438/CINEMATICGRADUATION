from django.contrib import admin
from .models import GraduationSettings, GraduateMessage


@admin.register(GraduationSettings)
class GraduationSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("🏫 معلومات المدرسة", {
            'fields': ('school_name', 'batch', 'ticker_text', 'card_speed')
        }),
        ("🖼️ الشعارات", {
            'fields': ('ministry_logo', 'school_logo')
        }),
    )

    def has_add_permission(self, request):
        return not GraduationSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(GraduateMessage)
class GraduateMessageAdmin(admin.ModelAdmin):
    list_display  = ('student_name', 'parent_name', 'is_active', 'created_at')
    list_filter   = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('student_name', 'parent_name')
    ordering      = ('-created_at',)
    readonly_fields = ('created_at',)

    fieldsets = (
        ("بيانات الرسالة", {
            'fields': ('student_name', 'parent_name', 'message', 'is_active', 'created_at')
        }),
    )


# تخصيص واجهة الأدمن
admin.site.site_header  = "إدارة حفل تخرج الطالبات"
admin.site.site_title   = "حفل التخرج ١٤٤٦"
admin.site.index_title  = "لوحة التحكم"
