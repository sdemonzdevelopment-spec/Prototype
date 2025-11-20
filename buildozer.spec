[app]

# 1. BASIC INFO
title = DemonZ
package.name = demonzgame
package.domain = org.demonz

# 2. FILES
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ogg

# 3. REQUIREMENTS - PRODUCTION READY WITH VERSION PINNING
# Pin Kivy version for stability and compatibility
requirements = python3==3.10,kivy==2.2.1,pillow==10.0.0,pyjnius

# 4. ANDROID SPECIFIC
version = 1.0.0
orientation = landscape
fullscreen = 1

# API Settings - Use stable API 33 instead of 34
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# ARCHITECTURES - Single arch for faster testing
# Change to: arm64-v8a,armeabi-v7a for production release
android.archs = arm64-v8a

# PERMISSIONS
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# 5. BUILD SETTINGS
android.private_storage = True

# Add app metadata
android.entrypoint = org.kivy.android.PythonActivity
android.apptheme = @android:style/Theme.NoTitleBar

[buildozer]
log_level = 2
warn_on_root = 1
