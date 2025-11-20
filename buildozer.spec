[app]

# 1. BASIC INFO
title = DemonZ
package.name = demonzgame
package.domain = org.demonz

# 2. FILES
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ogg

# 3. REQUIREMENTS
# We keep requirements standard. python3 implies the correct version for the p4a release.
requirements = python3,kivy==2.3.0,pillow,pyjnius==1.6.1

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

# CRITICAL FIX: Use a specific STABLE TAG instead of 'master' or 'develop'
# This version (Jan 2024) is stable and avoids the recent bugs.
p4a.branch = v2024.01.21

# 5. BUILD SETTINGS
android.private_storage = True

[buildozer]
log_level = 2
warn_on_root = 1
