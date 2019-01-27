from django.urls import path
from . import views
# from .views import ListSongsView

app_name = 'api'
urlpatterns = [
    # path('songs/', ListSongsView.as_view(), name="songs-all"),
    path('shelters/', views.ListShelterView, name="ListShelterView"),
]