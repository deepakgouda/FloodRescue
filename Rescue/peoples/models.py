from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
District_choices=[('','-------'),
                  ('Dist1','Dist1'),
                  ('Dist2','Dist2'),
                  ('Dist3','Dist3'),
                  ('Dist4','Dist4'),
                  ('Dist5','Dist5')
                  ]
gender =[
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
    ]
# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=51, blank=False, null=False, verbose_name="Name", default="Group")
    activeUser = models.IntegerField(default=1, blank=True)
    strength = models.IntegerField(default=1, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

class Person(models.Model):
    group = models.ForeignKey('Group',related_name='comments',on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=51, blank=False, null=False, verbose_name="Name",default="",)
    phone = models.CharField(max_length=14, null=True, blank=True, verbose_name='Mobile')
    aadhar=models.IntegerField(null=True,blank=True,verbose_name="Aadhar")
    age = models.IntegerField(null=True, blank=True, verbose_name="Age")
    gender = models.CharField(
        max_length=12,
        choices=gender,
        verbose_name='Gender',
        null=True, blank=True
    )
    location = models.CharField(max_length=100, blank=False, null=False, verbose_name="Location", default="Location")
    location_lat = models.FloatField(default=0, blank=True)
    location_log = models.FloatField(default=0, blank=True)
    address = models.TextField(max_length=150, null=True, blank=True, verbose_name="Address")
    district = models.CharField(
        max_length=15,
        choices=District_choices,
        verbose_name='Residence District',
        null=True, blank=True
    )
    status=models.IntegerField(null=True,blank=True,verbose_name="status")
    def __str__(self):
        return '{}-{}-{}'.format(self.name,self.aadhar,self.address)
class Shelter(models.Model):
    name=models.CharField(max_length=30,blank=True,default='')
    location_lat=models.FloatField(default=0,blank=True,)
    location_log = models.FloatField(default=0, blank=True,)
    capacity=models.IntegerField(default=0, blank=True, )
    used_capacity=models.IntegerField(default=0, blank=True, )
    resources_left=models.IntegerField(default=0,blank=True,)

    def __str__(self):
        return "{} -( {} , {} ) - {}".format(self.name, self.location_lat,self.location_log,self.capacity)


Area_volunterring_choices=[('','-------'),
                            ('dcr', 'Doctor'),
                            ('elw', 'Electrical Works'),
                            ('vls', 'Vehicle Support'),
                            ('rlo', 'Relief operation'),
                            ('cln', 'Cleaning'),
                            ('bot', 'Boat Service'),
                            ('oth', 'Other')
                        ]
class Volunteers(models.Model):
    name = models.CharField(max_length=30, blank=True, default='')
    district=models.CharField(max_length=50,choices=District_choices,default=' ')
    PersonID = models.IntegerField(default=-1, blank=True, )
    phone_no = models.IntegerField(default=9993993287, blank=True, )
    organisation=models.CharField(max_length=30, blank=True, default='')
    area_of_volunteering=models.CharField(max_length=50,choices=Area_volunterring_choices,default=' ')
    address=models.TextField()
    email=models.EmailField(null=True)

    def __str__(self):
        return "{} - {} - {}".format(self.name,self.phone_no,self.area_of_volunteering)

Need_choices=[('','-------'),
              ('resuce','Need Rescue'),
              ('resource','Need Resources'),
              ('both','Need Resue and Resources')]
class Request(models.Model):
    requestee_name=models.CharField(max_length=15,blank=True,default='')
    requestee_phone_no=models.IntegerField(blank=True,default=9993993287)
    requestee_location=models.CharField(max_length=5,blank=True,default='')
    location_lat = models.FloatField(default=0, blank=True, )
    location_log = models.FloatField(default=0, blank=True, )
    need = models.CharField(max_length=50, choices=Need_choices, default=' ')

    def __str__(self):
        return  self.need+" - "+self.requestee_location+" - "+str(self.requestee_phone_no)

class NGOS(models.Model):
    organisation_name=models.CharField(max_length=25,blank=True,default='')
    organisation_type=models.CharField(max_length=35,blank=True,default='')
    organisation_address=models.TextField()
    area_of_volunteering = models.CharField(max_length=50, choices=Area_volunterring_choices, default=' ')
    organisation_phone_no=models.IntegerField(blank=True,default=9993993287)

    def __str__(self):
        return self.organisation_name+" - "+str(self.organisation_phone_no)

class Missing_person(models.Model):
    name=models.CharField(max_length=25,blank=True,default='')
    aadhar=models.IntegerField(blank=True,default=1239819827839)
    age=models.IntegerField(blank=True,default=34)
    gender = models.CharField(
        max_length=12,
        choices=gender,
        verbose_name='Gender',
        null=True, blank=True
    )

    def __str__(self):
        return  self.name+"( "+str(self.age)+" , "+self.gender+" )"+" - "+str(self.aadhar)


# name
# age
# phone no
# aadhar
#
#
#
# address
# blood group
