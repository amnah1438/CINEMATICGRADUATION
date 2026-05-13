from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='graduationsettings',
            name='theme',
            field=models.CharField(default='gold-dark', max_length=50, verbose_name='الثيم'),
        ),
        migrations.AddField(
            model_name='graduationsettings',
            name='font',
            field=models.CharField(default='Tajawal', max_length=60, verbose_name='الخط'),
        ),
        migrations.AddField(
            model_name='graduationsettings',
            name='custom_primary',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='اللون الأساسي المخصص'),
        ),
        migrations.AddField(
            model_name='graduationsettings',
            name='custom_accent',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='لون الإضاءة المخصص'),
        ),
        migrations.AddField(
            model_name='graduationsettings',
            name='panel_password',
            field=models.CharField(default='1446', max_length=100, verbose_name='كلمة مرور لوحة الإدارة'),
        ),
        migrations.AddField(
            model_name='graduationsettings',
            name='default_grad_photo',
            field=__import__('cloudinary').models.CloudinaryField('صورة الخريجة الافتراضية', blank=True, folder='graduation/graduates', null=True),
        ),
    ]
