from django.urls import re_path

from firstapi.views import file_view

urlpatterns = [
    re_path(r'^(?P<version>(v1))/files/', file_view),
]
