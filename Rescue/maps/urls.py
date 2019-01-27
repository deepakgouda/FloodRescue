from django.conf.urls import url
from . import views

app_name = 'map'
urlpatterns = [
    url(r'^overview/$', views.overview, name='overview'),
    url(r'^vehicles/$', views.vehicles, name='vehicles'),
    url(r'^flooded/$', views.flooded, name='flooded'),
    url(r'^trial/$',views.trial,name='trial'),
    url(r'^shelter/$',views.shelter,name='shelter'),
]

