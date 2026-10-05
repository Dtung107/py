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
# LƯU Ý: Đã bổ sung cython phiên bản 0.29.33 để tránh lỗi biên dịch C-extensions
requirements = python3,kivy,pango,pandas,numpy,cython==0.29.33

# (str) Supported orientations
orientation = portrait

# (str) Bootstrap to use
p4a.bootstrap = sdl2

# (str) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Android API to target
android.api = 33

android.sdk = 33

android.minapi = 21

android.ndk_api = 21

android.ndk = 25c

android.skip_update = False

android.accept_sdk_license = True

# Buildozer section
[buildozer]

log_level = 2

warn_on_root = 1
