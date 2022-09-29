from xml.etree.ElementInclude import include
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("sign", views.sign, name="sign"),
    path("login", views.login_auth, name="login"),
    path("polling", views.polling, name="polling"),
    path("family", views.family, name= "family"),
    path("logout_auth", views.logout_auth, name= "logout_auth"),

]