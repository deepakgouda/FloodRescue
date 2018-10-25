from pymongo import MongoClient
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .forms import ShelterForm,Volunteer_registForm,RequestForm,MissingPersonForm,NGO_registForm
from .models import Missing_person,Request,Shelter,Volunteers,NGOS,Group,Person
from django.db.models import Q
from django.http import HttpResponse
import json
client_url="mongodb://yash-kothari:iNMDaoEEkYOPqHsTJ5cUigMb8wFWHsQGBaefdDNvSIwzEzjhtTGsHh20Ak6J3pH07lqid9CQxcg7Uet0UYLuYg==@yash-kothari.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = MongoClient(client_url)
db=client.django


# Create your views here.
def main_page(request):
    return render(request, 'peoples/main_page.html')


def person_finder(request):
    coll = db.shelter
    coll.insert_one({"name": "lll", "capacity": 111, "used_capacity": 0, "resource_left": 0, "location_lat": 20.144, "location_log": 83.79})
    coll.insert_one({"name": "ppp", "capacity": 222, "used_capacity": 0, "resource_left": 0, "location_lat": 19.391, "location_log": 82.38})
    coll.insert_one({"name": "qqq", "capacity": 333, "used_capacity": 0, "resource_left": 0, "location_lat": 19.30, "location_log": 83.94})
    coll.insert_one({"name": "qqq", "capacity": 333, "used_capacity": 0, "resource_left": 0, "location_lat": 20.69, "location_log": 86.56})
    return render(request, 'peoples/person_finder.html')


def all_shelters(request):
    shelters = db.shelter
    res = shelters.find()
    #res=[{"name":"Indore","resource_left":20,"used_capacity":10},{"name":"Odish","resource_left":500,"used_capacity":100},{"name":"Chennai","resource_left":40,"used_capacity":200},{"name":"India","resource_left":400,"used_capacity":1000},{"name":"rajpur","resource_left":400,"used_capacity":30}]
    return render(request, 'peoples/all_shelters.html', {'shelters': res})

def add_shelter(request):
    collection=db.shelter
    if request.method == "POST":
        form = ShelterForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['name'])
            # print(form.cleaned_data['capacity'])
            collection.insert_one({"name": form.cleaned_data['name'], "capacity": form.cleaned_data['capacity'],
                                   "location":form.cleaned_data["address"],
                                    "location_lat": form.cleaned_data["location_lat"],
                                   "location_log": form.cleaned_data["location_log"],
                                   "resources_left": 0, "used_capacity": 0})
            return redirect('peoples:add_shelter')
    else:
        form = ShelterForm()

    return render(request, 'peoples/add_shelter.html', {'form': form})


def volunteering(request):
    return render(request, 'peoples/volunteering.html')


def all_volunteers(request):
    personCol = db.person
    res = personCol.find({"Status": 3})
    #res=[{"name":"Bharti","address":"Odisha","contact":1237813912},{"name":"Kranti","address":"Indore","contact":23768712}]
    return render(request, 'peoples/all_volunteers.html', {'volunteers': res})


def volunteer_regist(request):
    req = request.method
    if req == "POST":
        form = Volunteer_registForm(request.POST)
        if form.is_valid():
            pid = req["PersonID"]

            personCol = db.person
            personCol.update({"PersonID": pid}, {"Status": 3})
            volunteer = form.save(commit=False)
            # post.author = get_object_or_404(Person,person_user=request.user)
            volunteer.save()
            return redirect('peoples:volunteer_regist')
    else:
        form = Volunteer_registForm()

    return render(request, 'peoples/volunteer_registration.html', {'form': form,})


def all_ngos(request):
    ngo_dict = db.NGO
    ngos = ngo_dict.find()
    #ngos=[{"name":"Bharti","address":"Odisha","contact":1237813912},{"name":"Kranti","address":"Indore","contact":23768712}]
    return render(request,'peoples/all_ngos.html',{'ngos':ngos})


def ngo_regist(request):
    if request.method == "POST":
        ngo = db.NGO
        form = NGO_registForm(request.POST)
        if form.is_valid():
            ngo.insert_one({"organisation_name": form.cleaned_data['organisation_name'],
                            "organisation_type": form.cleaned_data['organisation_type'],
                            "organisation_address": form.cleaned_data["organisation_address"],
                            "area_of_volunteering": form.cleaned_data["area_of_volunteering"],
                            "organisation_phone_no": form.cleaned_data["organisation_phone_no"]})
            return redirect('peoples:ngo_regist')
            # volunteer = form.save(commit=False)
            # post.author = get_object_or_404(Person,person_user=request.user)
            # volunteer.save()
            # return redirect('peoples:ngo_regist')
    else:
        form = NGO_registForm()

    return render(request, 'peoples/ngo_registration.html', {'form': form,})


def all_request(request):
    requestsCol = db.requests
    #requests = requestsCol.find()
    requests=[{"name":"Bharti","address":"Odisha","contact":1237813912},{"name":"Kranti","address":"Indore","contact":23768712}]

    return render(request,'peoples/all_request.html',{'requests':requests})


def make_request(request):
    req = db.requests
    print("view called")
    if request.method == "POST":
        form = RequestForm(request.POST)
        # print(form)
        # print("form posted")
        # print(form.is_valid())
        if form.is_valid():
            # print(form)
            req.insert_one({"requestee_name": form.cleaned_data['requestee_name'],
                            "requestee_phone_no": form.cleaned_data['requestee_phone_no'],
                            "requestee_location": form.cleaned_data["requestee_location"],
                            "location_lat": form.cleaned_data["location_lat"],
                            "location_log": form.cleaned_data["location_log"],
                            "need": form.cleaned_data["need"]
                            })
            # shelter = form.save(commit=False)
            # post.author = get_object_or_404(Person,person_user=request.user)
            # shelter.save()
            return redirect('peoples:make_request')
    else:
        form = RequestForm()

    return render(request, 'peoples/make_request.html', {'form': form,})


def missing_person_request(request):
    if request.method == "POST":
        # mis = db.missing
        form = MissingPersonForm(request.POST)
        if form.is_valid():
            # mis.insert_one({"name": form.cleaned_data['name'],
            #                 "aadhar": form.cleaned_data['aadhar'],
            #                 "age": form.cleaned_data["age"],
            #                 "gender": form.cleaned_data["gender"]})
            shelter = form.save(commit=False)
            post.author = get_object_or_404(Person,person_user=request.user)
            shelter.save()
            return redirect('peoples:missing_person_request')
    else:
        form = MissingPersonForm()

    return render(request, 'peoples/missing_person.html', {'form': form,})


def search_missing_person(request):
    # req = request.POST
    q = request.GET.get("q")
    res = []

    if q is None:
        return render(request, 'peoples/search_missing_person.html',
                      {'missing_persons': res, })
    personCol = db.person
    name = personCol.find({"Name": {'$regex': q, '$options': "i"}})
    aadhar = personCol.find({"Aadhar": q})
    phone = personCol.find({"Phone": q})

    # print(name + phone + aadhar)


    for i in name:
        res.append(i)

    for i in aadhar:
        res.append(i)

    for i in phone:
        res.append(i)
    print(res)
    return render(request, 'peoples/search_missing_person.html',
                  {'missing_persons': res,})


# App functions
@csrf_exempt
def add_group(request):
    req = request.POST
    print(req)
    s = True
    if req["GroupID"] == '-1':
        print("if")
        strength = len(req) - 2
        members = {}

        var = db.variables
        value = var.find_one({"ID": "gid"})['Value']
        var.update({"ID": "gid"}, {'$set': {"Value": value + 1}})

        for i in range(strength):
            personCol = db.person
            if personCol.find_one({"PersonID": int(req[str(i)])}) is None:
                s = False
                break
            personCol.update({"PersonID": int(req[str(i)])}, {'$set': {"GroupID": value}})
            members[req[str(i)]] = 1

        collection = db.group
        collection.insert_one({"GroupID": value, "activeUser": int(req["activeUser"]),
                               "Members": members})
    else:
        print("else")
        value = int(req["GroupID"])
        collection = db.group
        dict = collection.find_one({"GroupID": value})
        print(dict)
        members = dict['Members']

        newMembers = {}

        for i in range(len(req) - 2):
            if req[str(i)] in members:
                # print("ifin")
                newMembers[req[str(i)]] = members[req[str(i)]]
            else:
                # print("elsein")
                personCol = db.person
                if personCol.find_one({"PersonID": int(req[str(i)])}) is None:
                    s = False
                    break
                newMembers[req[str(i)]] = 1
                personCol.update({"PersonID": int(req[str(i)])}, {'$set': {"GroupID": value}})

        collection.update({"GroupID": value}, {'$set': {"Members": newMembers}})
    # print(value)
    # print(members)

    return HttpResponse(json.dumps({"GroupID": value, "Success": s}), content_type="application/json")


@csrf_exempt
def get_group(request):
    req=request.POST
    print(req)

    personCol = db.person
    gid = personCol.find_one({"PersonID": int(req['PersonID'])})['GroupID']

    var = db.group
    members = var.find_one({"GroupID": int(gid)})['Members']
    print(members)
    # var.update({"ID": "gid"}, {'$set': {"Value": value+1}})
    dict = {}

    j = 0
    for i in members:
        dict["person"+str(j)] = i
        j=j+1
    print(dict)
    return HttpResponse(json.dumps(dict), content_type="application/json")


@csrf_exempt
def print_POST_request(request):
    # if request.method == "POST":
    print(request.POST)
    req = request.POST
    var = db.variables
    value = var.find_one({"ID": "pid"})['Value']
    var.update({"ID": "pid"}, {'$set': {"Value": value + 1}})

    collection=db.person
    collection.insert_one({"GroupID": -1, "PersonID": value, "Name": req["name"], "Location_lat": 0,
                           "Location_long": 0, "PhoneNo": int(req["phonenumber"]), "Age": 340,
                           "Gender": "Male", "Status": -1,"Aadhar": int(req["aadhar"])
                           # "e-Mail": req["e-Mail"], "relative e-Mail": req["rel e-Mail"]
                            })
    return HttpResponse(json.dumps(value), content_type="application/json")


@csrf_exempt
def battery_stat(request):
    req = request.POST
    print(req)

    pid = req['PersonID']
    print(pid)

    personCol = db.person
    gid = personCol.find_one({"PersonID": int(pid)})["GroupID"]

    grp = db.group
    members = grp.find_one({"GroupID": gid})["Members"]

    currAct = grp.find_one({"GroupID": gid})["activeUser"]
    if not pid is currAct:
        return HttpResponse(json.dumps(currAct), content_type="application/json")

    members[str(pid)] = 0
    grp.update({"GroupID": "gid"}, {'$set': {"Members": members}})

    new_id = -1
    for i in members:
        if members[str(i)] is 1:
            new_id = i
            break
    # active_person=personCol.find_one({"PersonID": int(new_id)})
    # for i in members:
    #     curr_memb=personCol.find_one({"PersonID": int(i)})
    #     subject = "Number of "+curr_memb["Name"] +"is changed"
    #     from_email = settings.EMAIL_HOST_USER
    #     to_email = curr_memb["Sec_mail"]
    #     signup_message = "Now you can contact "+curr_memb["Name"] +"by calling at"+active_person["PhoneNo"]+"( "+active_person["Name"]+" )"
    #     send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message,
    #               fail_silently=False, )

    # `new_id` is the new active member. Send mail to all grp member's relatives regarding the new active member
    print(members)
    print(new_id)

    return HttpResponse(json.dumps(new_id), content_type="application/json")

@csrf_exempt
def is_active(request):
    req = request.POST
    print(req)

    pid = req['PersonID']

    personCol = db.person
    gid = personCol.find_one({"PersonID": pid})["GroupID"]

    grp = db.group
    actUser = grp.find_one({"GroupID": gid})["activeUser"]

    if pid is actUser:
        return HttpResponse(json.dumps("Yes"), content_type="application/json")
    else:
        return HttpResponse(json.dumps("No"), content_type="application/json")


@csrf_exempt
def search_missing_person_app(request):
    req = request.POST
    print(req)
    personCol = db.person

    # res = personCol.find({$or:[{"Aadhar": req["query"]}]})
    name = personCol.find({"Name": {'$regex': req['query'], '$options': "i"}})
    aadhar = personCol.find({"Aadhar": req["query"]})
    phone = personCol.find({"Phone": req["query"]})

    # print(name + phone + aadhar)

    res = []

    for i in name:
        res.append(i)

    for i in aadhar:
        res.append(i)

    for i in phone:
        res.append(i)
    print(res)

    for i in range(len(res)):
        res[i]["_id"] = ''

    return HttpResponse(json.dumps(res), content_type="application/json")
