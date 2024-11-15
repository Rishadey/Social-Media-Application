from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('testing',views.testing),
    path('registration',views.registration),
    path('registercode',views.registercode),
    path('del/<int:id>',views.dele),
    path('main',views.main),
    path('index',views.index),
    path('button',views.button),
    path('buttonlogin',views.buttonlogin),
    path('barbutton',views.barbutton),
    path('buttonhome',views.buttonhome),
    path('login',views.login),
    path('logincode',views.logincode),   
    path('post',views.post),
    path('upload',views.upload),
    path('upd',views.upd),
]
