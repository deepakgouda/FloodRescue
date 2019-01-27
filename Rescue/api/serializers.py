from rest_framework import serializers
from .models import Songs
from peoples.models import Shelter

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ("title", "artist")


class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shelter
        fields=('name','location_lat','location_log','capacity','used_capacity','resources_left')

