from django.conf.urls import url
from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.home, name='home1'),
    url(r'^home/$', views.home, name='home'),
]

