from django import forms

from .models import Shelter,Volunteers,Request,Missing_person,NGOS

class ShelterForm(forms.ModelForm):

    class Meta:
        model = Shelter
        fields = ('name', 'location_lat','location_log','capacity')

class Volunteer_registForm(forms.ModelForm):

    class Meta:
        model = Volunteers
        fields = ('PersonID', 'district', 'organisation', 'area_of_volunteering')

class NGO_registForm(forms.ModelForm):

    class Meta:
        model=NGOS
        fields=('organisation_name','organisation_type','organisation_address','area_of_volunteering','organisation_phone_no')



class RequestForm(forms.ModelForm):
    class Meta:
        model=Request
        fields=('requestee_name','requestee_phone_no','requestee_location','location_lat','location_log','need')

class MissingPersonForm(forms.ModelForm):

    class Meta:
        model=Missing_person
        fields=('name','aadhar','age','gender')
