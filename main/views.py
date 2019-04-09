from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Terr, Street, Number
from .forms import VisitForm, CreateForm
from django.shortcuts import render, get_object_or_404, HttpResponse, Http404, HttpResponseRedirect, render_to_response
from django.forms import modelformset_factory, inlineformset_factory, formset_factory
from django.views.decorators.csrf import csrf_exempt
import json
import datetime


class IndexView(TemplateView):
    template_name = 'html/index.html'


def all(request):
    terr = Terr.objects.all()
    context = {'t': terr}
    return render(request, 'html/all.html', context)


def test(request, pk):
    terr = Terr.objects.all()
    return render(request, 'html/test.html', {'t': terr, 'form': form, })


@csrf_exempt
def create_post(request, pk):
    if request.method == 'POST':
        number = request.POST.get('number')
        result = request.POST.get('results')
        pk = request.POST.get('idd')
        result = json.loads(result)
        selectNumber = Number.objects.get(pk=pk)
        try:
            for num in result:
                if len(result[num]) != 0:
                    print(num)
                    if num == '0':
                        selectNumber.visit1 = result[num]
                    if num == '1':
                        selectNumber.visit2 = result[num]
                    if num == '2':
                        selectNumber.visit3 = result[num]
                    if num == '3':
                        selectNumber.notes = result[num]
                    selectNumber.save()

        except KeyError:
            print('error key')
        return HttpResponse(
            json.dumps({"workesd": "ayeeeeee", "lol": number}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def detail(request, pk):
    form = VisitForm()
    terr = Terr.objects.get(pk=pk)
    if terr.street_set.all():
        form = VisitForm()
        terr = get_object_or_404(Terr, pk=pk)
        return render(request, 'html/details.html', {'t': terr, 'form': form})
    else:
        return render(request, 'html/details.html', {'t': terr})

def streetdeets(request, pk, streetpk):
    street = Street.objects.get(pk=streetpk)
    return render(request, 'html/street_details.html', {'street': street})

def spliter(input):
    hello = list()
    words = input.split(',')
    for word in words:
        hello.append(word)
    return hello

@csrf_exempt
def addstreet(request, pk):
    if request.method == 'POST':
        holdup = request.POST['streetName']
        func = spliter(holdup)
        selected_terr = Terr.objects.get(pk=pk)
        for new in func:
            newnew = Street()
            newnew.name = new
            newnew.date_worked = datetime.datetime.now()
            newnew.terr = selected_terr
            newnew.save()
        return HttpResponse(
            json.dumps({"workesd": "ayeeeeee", "lol": 'lol'}),
            content_type="application/json"
        )


@csrf_exempt
def addnumber(request, pk):
    if request.method == 'POST':
        selected_street = Street.objects.get(pk=request.POST['pk'])
        sent_data = request.POST['numberValue']
        func = spliter(sent_data)
        for new in func:
            print(new)
            newnewnum = Number()
            newnewnum.value = new
            newnewnum.street = selected_street
            newnewnum.save()
        return HttpResponse(
            json.dumps({"workesd": "ayeeeeee", "lol": 'lol'}),
            content_type="application/json"
        )


def create_terr(request):
    if request.method == 'POST':
        print(request.POST)
        form = CreateForm(request.POST)
        if form.is_valid():
            obj = Terr()
            obj.num = form.cleaned_data['num']
            obj.sub = form.cleaned_data['sub']
            obj.owner = form.cleaned_data['owner']
            obj.lat_cordinate = form.cleaned_data['lat_cordinate']
            obj.long_cordinate = form.cleaned_data['long_cordinate']
            obj.save()
            print('cappichi')
        return render(request, 'main/terr_form.html', {'form': form})

    else:
        form = CreateForm()
        return render(request, 'main/terr_form.html', {'form': form})