from django.shortcuts import render
from pymongo import MongoClient
from django.http import HttpResponse
import json

client_url="mongodb://yash-kothari:iNMDaoEEkYOPqHsTJ5cUigMb8wFWHsQGBaefdDNvSIwzEzjhtTGsHh20Ak6J3pH07lqid9CQxcg7Uet0UYLuYg==@yash-kothari.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = MongoClient(client_url)
db=client.django

# Create your views here.
def trial(request):
    return render(request,'maps/trial.html')
def overview(request):
    #both location and address are must address is used in showing multiple paths together
    locations=[[47.50832, -1.12715,'NGO1','Newyork'],[51.51672, 0.12750,'NGO2','London'],[52.51832, -0.72784,'NGO3','India'],[45.10632, -0.32514,'NGO4','America'],[51.20432, -0.10714,'NGO5','Japan'],[26.177685, 91.781624,'NGO6','Shilong']]
    return render(request, 'maps/main_page.html',{'locations':locations})

def flooded(request):
    # col = db.substation
    # coll = []
    #
    # for i in col.find():
    #     coll.append([i['location_lat'], i['location_log']])
    coll=[[19.602,86.003],[18.7228,84.838],[18.089,84.333]]
    print(coll)
    return render(request, 'maps/flooded.html',{'locations':coll})

def shelter(request):
    col = db.shelter
    coll = []

    for i in col.find():
        coll.append([i['location_lat'],i['location_log']])

    print(coll)
    return render(request, 'maps/shelter.html',{'locations':coll})

def vehicles(request):
    routes=[[[47.50832, -1.12715,'NGO1','Bellevue, WA'],[51.51672, 0.12750,'NGO2','Seattle, WA']],
            [[52.51832, -0.72784,'NGO3','Kirkland'],[45.10632, -0.32514,'NGO4','Bothell , WA']],
            [[47.50832, -1.12715, 'NGO1', 'Woodinville, WA'], [51.51672, 0.12750, 'NGO2', 'Duval, WA']],
            [[52.51832, -0.72784, 'NGO3', 'Redmond, WA'], [45.10632, -0.32514, 'NGO4', 'Sammamish, WA']]]
    sources=[[47.50832, -1.12715,'NGO1','Bellevue, WA'],[52.51832, -0.72784,'NGO3','Kirkland'],[47.50832, -1.12715, 'NGO1', 'Woodinville, WA'],[52.51832, -0.72784, 'NGO3', 'Redmond, WA']]
    destinations=[[51.51672, 0.12750,'NGO2','Seattle, WA'],[45.10632, -0.32514,'NGO4','Bothell , WA'],[51.51672, 0.12750, 'NGO2', 'Duval, WA'],[45.10632, -0.32514, 'NGO4', 'Sammamish, WA']]
    return render(request, 'maps/vehicles.html',{'routes':routes,'sources':sources,'destinations':destinations})
