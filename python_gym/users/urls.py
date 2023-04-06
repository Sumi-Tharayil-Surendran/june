from django.contrib import admin
from django.urls import include, path
from users.views import login
from users.views import register
from users.views import logout,activate,activation_sent_view

urlpatterns = [
    path("", include("mainapp.urls")),
    path("register", register, name="register"),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    #path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('sent/', activation_sent_view, name="activation_sent")
]
