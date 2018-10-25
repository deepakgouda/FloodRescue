from django.contrib import admin
from .models import Shelter,Person,Volunteers,Missing_person,NGOS,Request,Group

admin.site.register(Shelter)
admin.site.register(Person)
admin.site.register(Volunteers)
admin.site.register(Missing_person)
admin.site.register(NGOS)
admin.site.register(Request)
admin.site.register(Group)
