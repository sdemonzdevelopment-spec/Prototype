[app]

# 1. BASIC INFO
title = DemonZ
package.name = demonzgame
package.domain = org.demonz

# 2. FILES
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ogg

# 3. REQUIREMENTS - SIMPLIFIED (no version pinning to avoid 404 errors)
requirements = python3==3.10.13,kivy==2.3.0,pillow,pyjnius==1.6.1,hostpython3==3.10.13

# 4. ANDROID SPECIFIC
version = 1.0.0
orientation = landscape
fullscreen = 1

# API Settings
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# ARCHITECTURES - Single arch for faster builds
android.archs = arm64-v8a

# PERMISSIONS
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# 5. BUILD SETTINGS
android.private_storage = True
android.entrypoint = org.kivy.android.PythonActivity
android.apptheme = @android:style/Theme.NoTitleBar

# Use master branch for latest bug fixes
# p4a.branch = master


[buildozer]
log_level = 2
warn_on_root = 1
