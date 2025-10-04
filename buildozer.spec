[app]
title = Калькулятор
package.name = calculator
package.domain = org.missr

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0
requirements = python3,kivy

orientation = portrait

[buildozer]
log_level = 2

[app]
android.permissions = INTERNET

[app]
android.api = 33
android.minapi = 21
