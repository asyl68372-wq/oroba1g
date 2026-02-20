[app]
title = My App
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# المتطلبات الأساسية فقط لضمان خفة الحجم
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# إعدادات التوافق القصوى مع سيرفرات GitHub
android.api = 33
android.minapi = 21
android.ndk = 25b
android.skip_setup_py = 1

# أهم سطر: بناء معمارية واحدة فقط لمنع استهلاك المساحة والفشل
android.archs = arm64-v8a

# تفعيل التنظيف التلقائي الداخلي
android.copy_libs = 1
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
