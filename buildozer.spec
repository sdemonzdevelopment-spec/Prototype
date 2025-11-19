[app]

# 1. BASIC INFO
title = DemonZ
package.name = demonzgame
package.domain = org.demonz

# 2. FILES
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ogg

# 3. REQUIREMENTS
# We use pyjnius 1.6.1 for Python 3 compatibility
# We include hostpython3 which is often needed for the build process
requirements = python3,kivy==2.3.0,pillow,pyjnius==1.6.1,hostpython3

# 4. ANDROID SPECIFIC
version = 0.1
orientation = landscape
fullscreen = 1

# API Settings (Standard for 2025)
android.api = 34
android.minapi = 21
android.accept_sdk_license = True

# ARCHITECTURES
# Supports both modern and older devices
android.archs = arm64-v8a, armeabi-v7a

# CRITICAL SETTINGS FOR PYTHON 3 & KIVY 2.3.0
# We use the develop branch to get the latest fixes for Android 14 (API 34)
p4a.branch = develop

# 5. BUILD SETTINGS
android.private_storage = True

[buildozer]
log_level = 2
warn_on_root = 1
