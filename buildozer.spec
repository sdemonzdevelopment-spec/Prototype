[app]

# 1. BASIC INFO
title = DemonZ
package.name = demonzgame
package.domain = org.demonz

# 2. FILES
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ogg

# 3. REQUIREMENTS
# Using newer, working versions - no version pins for auto-compatibility
requirements = python3,kivy,pillow,pyjnius

# 4. ANDROID SPECIFIC
version = 0.1
orientation = landscape
fullscreen = 1

# API Settings (API 34 is supported by this release)
android.api = 34
android.minapi = 21
android.accept_sdk_license = True

# ARCHITECTURES
android.archs = arm64-v8a, armeabi-v7a

# CRITICAL FIX: Use the latest stable release
# Using develop branch for latest bug fixes and Python 3 compatibility
p4a.branch = develop

# 5. BUILD SETTINGS
android.private_storage = True

[buildozer]
log_level = 2
warn_on_root = 1
