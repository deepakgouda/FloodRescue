from rest_framework import generics
from .models import Songs
from peoples.models import Shelter
from django.views.decorators.csrf import csrf_exempt
from .serializers import SongsSerializer, ShelterSerializer
from pymongo import MongoClient
from django.http import HttpResponse
import json

client_url="mongodb://yash-kothari:iNMDaoEEkYOPqHsTJ5cUigMb8wFWHsQGBaefdDNvSIwzEzjhtTGsHh20Ak6J3pH07lqid9CQxcg7Uet0UYLuYg==@yash-kothari.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = MongoClient(client_url)
db=client.django

class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

@csrf_exempt
def ListShelterView(request):
    """
    Provides a get method handler.
    """
    col = db.shelter
    coll = []

    for i in col.find():
        coll.append(i)

    # print(coll)

    for i in coll:
        i["_id"] = ''
    return HttpResponse(json.dumps(coll), content_type="application/json")