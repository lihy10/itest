@echo off
set DJANGO_SETTINGS_MODULE=autotest_platform.settings
daphne -b 0.0.0.0 -p 8000 autotest_platform.asgi:application 