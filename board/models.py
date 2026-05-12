from django.db import models
from cloudinary.models import CloudinaryField


class GraduationSettings(models.Model):
    school_name = models.CharField(
        max_length=200,
        default="الثانوية الثالثة عشرة بعرعر",
        verbose_name="اسم المدرسة"
    )
    batch = models.CharField(
        max_length=200,
        default="دفعة الفخر والعطاء · ١٤٤٦ هـ",
        verbose_name="اسم الدفعة"
    )
    ticker_text = models.CharField(
        max_length=300,
        default="مبارك للخريجات العزيزات",
        verbose_name="نص شريط الأخبار"
    )
    ministry_logo = CloudinaryField(
        'شعار وزارة التعليم',
        folder='graduation/logos',
        blank=True, null=True,
    )
    school_logo = CloudinaryField(
        'شعار المدرسة',
        folder='graduation/logos',
        blank=True, null=True,
    )
    card_speed = models.PositiveIntegerField(
        default=9,
        verbose_name="مدة عرض كل بطاقة (ثانية)"
    )

    class Meta:
        verbose_name = "إعدادات الحفل"
        verbose_name_plural = "إعدادات الحفل"

    def __str__(self):
        return "إعدادات حفل التخرج"

    def save(self, *args, **kwargs):
        # يسمح بسجل واحد فقط
        self.pk = 1
        super().save(*args, **kwargs)


class GraduateMessage(models.Model):
    student_name = models.CharField(max_length=100, verbose_name="اسم الطالبة")
    parent_name  = models.CharField(max_length=100, verbose_name="اسم ولي الأمر")
    message      = models.TextField(verbose_name="الرسالة")
    is_active    = models.BooleanField(default=True, verbose_name="تظهر في العرض")
    created_at   = models.DateTimeField(auto_now_add=True, verbose_name="وقت الإرسال")

    class Meta:
        verbose_name = "رسالة خريجة"
        verbose_name_plural = "رسائل الخريجات"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student_name} — {self.parent_name}"
