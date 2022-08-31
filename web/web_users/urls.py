from django.urls import path

from web.web_users.views import demo

urlpatterns = [
    path('demo/', demo, name='demo'),
]
