from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Terr, Street, Number
from django.template import loader
# Create your views here.
def index(request):
    return render(request, 'html/index.html')

def detail(request, num):
    try:
        terr = Terr.objects.get(pk=num)
    except Terr.DoesNotExist:
        raise Http404("whats are you seraching for")
    return render(request, 'html/details.html', {'terr': terr})

def all(request):
    all_terr = Terr.objects.all()
    context = {'all_terr': all_terr}
    return render(request, 'html/all.html', context)
