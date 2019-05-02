from django import forms
from django.contrib.auth.models import User

class VisitForm(forms.Form):
    visit1 = forms.CharField(max_length=2, required=False)
    visit2 = forms.CharField(max_length=2, required=False)
    visit3 = forms.CharField(max_length=2, required=False)
    notes = forms.CharField(max_length=50, required=False)

class CreateForm(forms.Form):
    num = forms.CharField(max_length=6)
    sub = forms.CharField(max_length=30)
    owner = forms.CharField(max_length=40)
    lat_cordinate = forms.FloatField()
    long_cordinate = forms.FloatField()

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class CreateUser(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
