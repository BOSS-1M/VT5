
# ملف تشغيل للوحدة المشفرة VT5.cpython-313-aarch64-linux-android.so
import VT5

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(VT5, 'main'):
    VT5.main()
else:
    print("تم استيراد VT5 بنجاح، ولكن لا توجد دالة main للتشغيل.")
