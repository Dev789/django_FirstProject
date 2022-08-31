from django.urls import path, re_path

from firstapp.views import hello_world, user_insert, get_user, user_update, ApiHelloWorld, get_data

urlpatterns = [
    path('user/', hello_world, name='user'),
    re_path(r'^(?P<version>(v1))/user/insert/', user_insert, name='user_insert'),
    re_path(r'^(?P<version>(v1))/user/data/', get_data, name='get_data'),
    re_path(r'^(?P<version>(v1))/user/list/', get_user, name='get_user'),
    re_path(r'^(?P<version>(v1))/user/update/(?P<pk>[0-9]+)', user_update, name='user_update'),
    re_path(r'^(?P<version>(v1))/user/lang/', ApiHelloWorld.as_view(), name='api_hello_world'),
    # path('users/', include('firstapp.urls'))
]
