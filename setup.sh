#!/bin/bash
# ====================================================
#  إعداد مشروع حفل التخرج — يُشغَّل مرة واحدة فقط
# ====================================================
cd "$(dirname "$0")"
echo ""
echo "  🎓 إعداد مشروع حفل تخرج الطالبات"
echo "  ─────────────────────────────────"

# 1. إنشاء البيئة الافتراضية
echo "  ⏳ إنشاء البيئة الافتراضية..."
python3 -m venv venv
source venv/bin/activate
echo "  ✅ البيئة جاهزة ($(python --version))"

# 2. تثبيت الحزم
echo "  ⏳ تثبيت الحزم..."
pip install -q -r requirements.txt
echo "  ✅ تم تثبيت الحزم"

# 3. Migrations
echo "  ⏳ إنشاء قاعدة البيانات..."
python manage.py migrate --run-syncdb
echo "  ✅ قاعدة البيانات جاهزة"

# 4. إنشاء المشرف
echo ""
echo "  ─────────────────────────────────"
echo "  📋 إنشاء حساب الأدمن:"
python manage.py createsuperuser

echo ""
echo "  ✅ الإعداد اكتمل! شغّلي السيرفر بـ:"
echo "     bash run.sh"
echo ""
