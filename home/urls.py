# from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("sign", views.sign, name="sign"),
    path("login", views.login, name="login"),
]