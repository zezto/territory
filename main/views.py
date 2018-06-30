from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Terr, Street, Number
from django.template import loader
# Create your views here.
def index(request):
    return render(request, 'html/index.html')

def detail(request, num):
    terr = get_object_or_404(Terr, pk=num)

    return render(request, 'html/details.html', {'terr': terr})

def all(request):
    all_terr = Terr.objects.all()
    context = {'all_terr': all_terr}
    return render(request, 'html/all.html', context)
