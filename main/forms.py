from django import forms

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