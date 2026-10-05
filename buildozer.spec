[app]

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
# LƯU Ý: Chỉ sử dụng các thư viện cần thiết để tránh lỗi biên dịch
requirements = python3,kivy==2.3.0

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

# (bool) Use the new Gradle system
android.gradle_dependencies =

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

# (list) Services to declare
android.services =

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (str) Android logcat filters to use (default is *:S python:D)
# android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (str) Android app theme, default is ok for Kivy-based app
# android.theme = "@android:style/Theme.NoTitleBar"

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (str) Android logcat filters to use (default is *:S python:D)
# android.logcat_filters = *:S python:D

# (str) Android Bootstrap to use
# android.bootstrap = sdl2

android.skip_update = False

android.accept_sdk_license = True

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will be disabled.
# android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
# android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file for custom backup agent declaration inside the AndroidManifest.xml:
# see http://developer.android.com/guide/topics/data/keyvaluebackup.html
# android.backup_agent_xml =

# (str) Class for custom backup agent. This class must be subclassed from
# android.app.backup.BackupAgent
# android.backup_agent_class =

# (str) Log level (0 = error only, 1 = info, 2 = debug (with command output))
# android.logcat_filters = *:S python:D

# (bool) Indicate if the application should be fullscreen or not
# fullscreen = 0

# (str) Orientation of the application, landscape or portrait
# or sensor to choose depending on the sensor
# orientation = portrait

# (bool) Indicate if the status bar should be visible (Android only)
# android.statusbar_hidden = False

# (list) Permissions
# android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
# android.api = 30

# (int) Minimum API your APK will support.
# android.minapi = 21

# (int) Android SDK version to use
# android.sdk = 30

# (str) Android NDK version to use
# android.ndk = 21

# (int) Android NDK API to use.
# android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
# android.private_storage = True

# (str) Android app theme, default is ok for Kivy-based app
# android.theme = "@android:style/Theme.NoTitleBar"

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# android.archs = arm64-v8a,armeabi-v7a

# (int) overrides automatic versionCode computation from version.x.y.z
# android.version_code = 1

# (list) pattern matched against the release version number used to
# provide the PlayStore versionCode. If blank, the following pattern is used to
# compute the versioncode from version.x.y.z:
#     (.+)\.(.+)\.(.+) will be replaced by 10000 * int(x) + 100 * int(y) + int(z);
# android.release_artifact = apk

# (str) Android logcat filters to use (default is *:S python:D)
# android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# android.archs = arm64-v8a,armeabi-v7a

# (bool) Enable AndroidX support
# android.enable_androidx = True

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# android.archs = arm64-v8a,armeabi-v7a

# (bool) Enable AndroidX support
# android.enable_androidx = True

# (list) Pattern to whitelist for the whole project
#android.whitelist = lib-dynload/collections.so

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (str) Android logcat filters to use (default is *:S python:D)
# android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (str) Android Bootstrap to use, default is sdl2
# android.bootstrap = sdl2

# (int) port number to specify user port
# android.port = 8000

# (str) Android logcat filters to use (default is *:S python:D)
# android.logcat_filters = *:S python:D

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = .buildozer

# (str) Path to build output (i.e. .apk, .aab)
# bin_dir = ./bin
