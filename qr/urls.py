from django.conf.urls import url

from . import views

app_name = "qr"
urlpatterns = [
    url(r"^$", views.signin, name="login"),
    url(r"^logout/$", views.signout, name="logout"),
    url(r"^home/$", views.home, name="home"),
    url(r"^curso/(?P<id_curso>[0-9]+)/$", views.curso, name="curso"),
    url(r"^clase_activa/(?P<id_curso>[0-9]+)/(?P<id_clase>[0-9]+)/$", views.clase, {'active': True}, name="clase_activa"),
    url(r"^clase/(?P<id_curso>[0-9]+)/(?P<id_clase>[0-9]+)/$", views.clase,{'active': False}, name="clase"),
]