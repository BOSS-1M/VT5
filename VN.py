
# ملف تشغيل للوحدة المشفرة VN.cpython-313-aarch64-linux-android.so
import VN

# تأكد أن الدالة الرئيسية موجودة داخل الملف الأصلي
if hasattr(VN, 'main'):
    VN.main()
else:
    print("تم استيراد VN بنجاح، ولكن لا توجد دالة main للتشغيل.")
