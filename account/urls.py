from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('enterphone', views.enter_phone, name='enter_phone'),
    path('check', views.enter_code, name='check'),
    path('register', views.register, name='register'),
    path('logout', views.logout_user, name='logout'),
    path('address', views.address, name='address'),

]
