[app]

# 1. BASIC INFO
title = DemonZ
package.name = demonzgame
package.domain = org.demonz

# 2. FILES
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ogg

# 3. REQUIREMENTS
# Added hostpython3, which is often required for GitHub Actions builds
requirements = python3,kivy==2.3.0,pillow,hostpython3

# 4. ANDROID SPECIFIC
version = 0.1
orientation = landscape
fullscreen = 1

# API Settings (Standard for 2025)
android.api = 34
android.minapi = 21
# It is usually safer to let Buildozer download the NDK it needs automatically.
# android.ndk = 25b 
android.accept_sdk_license = True

# ARCHITECTURES
# Adding armeabi-v7a ensures it works on older cheap phones too, not just new ones.
android.archs = arm64-v8a, armeabi-v7a

# 5. BUILD SETTINGS
android.private_storage = True

[buildozer]
log_level = 2
warn_on_root = 1
