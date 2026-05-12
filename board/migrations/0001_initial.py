from django.db import migrations, models
import cloudinary.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GraduationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(default='الثانوية الثالثة عشرة بعرعر', max_length=200, verbose_name='اسم المدرسة')),
                ('batch', models.CharField(default='دفعة الفخر والعطاء · ١٤٤٦ هـ', max_length=200, verbose_name='اسم الدفعة')),
                ('ticker_text', models.CharField(default='مبارك للخريجات العزيزات', max_length=300, verbose_name='نص شريط الأخبار')),
                ('ministry_logo', cloudinary.models.CloudinaryField(blank=True, null=True, verbose_name='شعار وزارة التعليم')),
                ('school_logo', cloudinary.models.CloudinaryField(blank=True, null=True, verbose_name='شعار المدرسة')),
                ('card_speed', models.PositiveIntegerField(default=9, verbose_name='مدة عرض كل بطاقة (ثانية)')),
            ],
            options={
                'verbose_name': 'إعدادات الحفل',
                'verbose_name_plural': 'إعدادات الحفل',
            },
        ),
        migrations.CreateModel(
            name='GraduateMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100, verbose_name='اسم الطالبة')),
                ('parent_name', models.CharField(max_length=100, verbose_name='اسم ولي الأمر')),
                ('message', models.TextField(verbose_name='الرسالة')),
                ('is_active', models.BooleanField(default=True, verbose_name='تظهر في العرض')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='وقت الإرسال')),
            ],
            options={
                'verbose_name': 'رسالة خريجة',
                'verbose_name_plural': 'رسائل الخريجات',
                'ordering': ['-created_at'],
            },
        ),
    ]
