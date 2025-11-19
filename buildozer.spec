[app]

# 1. BASIC INFO
title = DemonZ
package.name = demonzgame
package.domain = org.demonz

# 2. FILES
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ogg

# 3. REQUIREMENTS
# Using 'python3' lets Buildozer pick the correct stable version (likely 3.11.9)
# We keep hostpython3 as it is required for the build process
requirements = python3,kivy==2.3.0,pillow,pyjnius==1.6.1,hostpython3

# 4. ANDROID SPECIFIC
version = 0.1
orientation = landscape
fullscreen = 1

# API Settings
android.api = 34
android.minapi = 21
android.accept_sdk_license = True

# ARCHITECTURES
android.archs = arm64-v8a, armeabi-v7a

# CRITICAL FIX: Use 'master' branch to avoid broken remote debugging code
p4a.branch = master

# 5. BUILD SETTINGS
android.private_storage = True

[buildozer]
log_level = 2
warn_on_root = 1
