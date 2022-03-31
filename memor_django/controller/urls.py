from django.urls import path
from . import views

app_name = 'contorller'
urlpatterns = [
    path('home/',views.login_info,name='info'),
    path('data/',views.get_login,name="getUser"),
    path('downloads/',views.get_image,name='senImage')
]