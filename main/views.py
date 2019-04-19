from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.views.generic import TemplateView, View
from django.urls import reverse_lazy
from .models import Terr, Street, Number
from .forms import VisitForm, CreateForm, UserLoginForm
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect, HttpResponseRedirect, render_to_response
from django.forms import modelformset_factory, inlineformset_factory, formset_factory
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
import qrcode
import os
from pathlib import Path
from django.contrib.auth import authenticate, login


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

QR_ROOT = os.path.join('main/static/QR/')


class UserFormView(View):
    template_name = 'html/index.html'
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:all')
            else:
                return render(request, self.template_name, {'form': form, 'code': '1'})

        else:
            return render(request, self.template_name, {'form': form, 'code': '2'})


def all(request):
    terr = Terr.objects.all()
    context = {'t': terr}
    return render(request, 'html/all.html', context)


def test(request, pk):
    terr = Terr.objects.all()
    return render(request, 'html/test.html', {'t': terr, 'form': form, })


@csrf_exempt
def create_post(request, pk, streetpk):
    if request.method == 'POST':
        number = request.POST.get('number')
        result = request.POST.get('results')
        pk = request.POST.get('idd')
        result = json.loads(result)
        selectNumber = Number.objects.get(pk=pk)
        try:
            for num in result:
                if len(result[num]) != 0:
                    if num == '0':
                        selectNumber.visit1 = result[num]
                        selectNumber.date_worked1 = str(datetime.date.today().strftime('%b %d,%Y'))
                    if num == '1':
                        selectNumber.visit2 = result[num]
                        selectNumber.date_worked2 = str(datetime.date.today().strftime('%b %d,%Y'))


                    if num == '2':
                        selectNumber.visit3 = result[num]
                        selectNumber.date_worked3 = str(datetime.date.today().strftime('%b %d,%Y'))


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
    pathtoqr = Path(QR_ROOT+'%s.jpeg' % pk)
    if pathtoqr.is_file():
        pass
    else:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        data = '10.0.0.4:8000/%s/ ' % pk
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        final = QR_ROOT + '%s.jpeg' % pk
        img.save(final)
    if terr.street_set.all():
        terr = get_object_or_404(Terr, pk=pk)
        return render(request, 'html/details.html', {'t': terr, 'form': form})
    else:
        return render(request, 'html/details.html', {'t': terr})


def streetdeets(request, pk, streetpk):
    street = Street.objects.get(pk=streetpk)
    form = VisitForm()
    first_num = street.number_set.all().first()
    pathtostreetqr = Path(QR_ROOT + 'street_%s' % streetpk)
    if pathtostreetqr.is_file():
        pass
    else:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        data = '10.0.0.4:8000/%s/%s ' % (pk, streetpk)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        final = QR_ROOT + 'street-%s.jpeg' % streetpk
        img.save(final)

    return render(request, 'html/street_details.html', {'street': street,'f':first_num, 'form': form})


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
def addnumber(request, pk, streetpk):
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
