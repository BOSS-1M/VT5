
# ملف تشغيل للوحدة المشفرة VN.cpython-313-aarch64-linux-android.so
import VN

# قائمة بأسماء الدوال الممكنة للتشغيل
possible_functions = ['main', 'menu', 'run', 'start', 'execute', 'run_tool', 'start_tool']

found = False
for func_name in possible_functions:
    if hasattr(VN, func_name):
        print(f"[✔] تشغيل الدالة: {func_name}")
        getattr(VN, func_name)()
        found = True
        break

if not found:
    print("[!] لم يتم العثور على دالة رئيسية (main, menu, run, start)")
    print("[!] قائمة الدوال المتوفرة:")
    for attr in dir(VN):
        if not attr.startswith('_') and callable(getattr(VN, attr)):
            print(f"    - {attr}")
