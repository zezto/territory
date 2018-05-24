from django.shortcuts import render
from django.http import HttpResponse
from .models import Terr
from django.template import loader
# Create your views here.
def index(request):
    return render(request, 'html/index.html')

def detail(request, num):
    return HttpResponse("<h1> LOl " + str(num) + "</h1>")

def all(request):
    all_terr = Terr.objects.all()
    context = {'all_terr': all_terr}
    return render(request, 'html/all.html', context)
