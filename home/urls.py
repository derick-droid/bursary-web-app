# from xml.etree.ElementInclude import include
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("sign", views.sign, name="sign"),
    path("login", views.login, name="login"),
    path("polling", views.polling, name="polling"),
    path("family", views.family, name= "family"),
]