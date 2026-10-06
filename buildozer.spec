l[app]

# (str) Title of your application
title = Game Quay So

# (str) Package name
package.name = quaysogame

# (str) Package domain (needed for android/ios packaging)
package.domain = org.quaysogame

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (process one by one)
source.include_exts = py,kv,png,jpg,gif,mp4,mp3,ttf,ttc

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy==2.3.0,cython==0.29.33

# (str) Supported orientations
orientation = portrait

# (str) Android logcat filters to use (default is *:S python:D)
android.logcat_filters = *:S python:D

# (list) Pattern matched against the release version number used to mark
# full releases as candidate for the Play Store's staged rollout
android.release_artifact = apk

# (int) Target Android API level
android.api = 33

# (int) Minimum API level to target
android.minapi = 21

# (str) Android NDK version to target
android.ndk = 25b

# (str) Android NDK API level to target
android.ndk_api = 21

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (bool) Enable AndroidX support
android.enable_androidx = True

# (list) Pattern to whitelist for the whole project
android.whitelist = lib-dynload/collections.so

# (list) Application permissions
android.permissions = INTERNET

# (bool) Skip SDK/NDK update
android.skip_update = False

# (bool) Accept Android SDK license
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
