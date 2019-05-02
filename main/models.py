from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime

class Terr(models.Model):
    num = models.IntegerField(default=0)
    sub = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_favorite = models.BooleanField(default=False)
    lat_cordinate = models.FloatField(default=0)
    long_cordinate = models.FloatField(default=0)

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.num) + ' ' + self.sub + ' - ' + str(self.owner.get_full_name())

    def nc_percent(self):
        street_of_terr = Street.objects.filter(terr=self.pk)
        percents = list()
        final = 0
        for street in street_of_terr:
            percents.append(street.nc_percent())
        for percent in percents:
            final+=percent
        final = round(final/len(percents),2)
        return final
    
    def number_count(self):
        nums = Number.objects.filter(street__terr=self.pk).count()
        return nums

class Street(models.Model):
    name = models.CharField(max_length=100)
    date_worked = models.DateField(auto_now_add=True)
    terr = models.ForeignKey(Terr, on_delete=models.CASCADE)
    last_updated = models.DateField(auto_now=True, null=True)
    last_login = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def nc_percent(self):
        num_of_street = Number.objects.filter(street=self.pk)
        percents = list()
        final = 0
        for num in num_of_street:
            percents.append(num.nc_percent())
        for percent in percents:
            final+=percent
        final = round(final / len(percents), 2)
        return final
    
    def count_of_number(self):
        numbers = Number.object.filter(street=self.pk).count()
        return numbers

class Number(models.Model):
    value = models.IntegerField(default=0)
    visit1 = models.CharField(max_length=100, blank=True)
    visit2 = models.CharField(max_length=100, blank=True)
    visit3 = models.CharField(max_length=100, blank=True)
    notes = models.CharField(max_length=100, blank=True)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    date_worked1 = models.CharField(max_length=150, blank=True)
    date_worked2 = models.CharField(max_length=150, blank=True)
    date_worked3 = models.CharField(max_length=150, blank=True)
    last_updated = models.TimeField(auto_now=True, null=True)
    last_updated_date = models.DateField(auto_now=True, null=True)
    last_login = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['value']

    def __str__(self):
        return str(self.value)

    def nc_percent(self):
        nc_percent = [self.visit1,self.visit2, self.visit3]
        test = list()
        for x in nc_percent:
            if x != '':
                test.append(x)
        lol = test.count('nc')
        percent = round((lol / 3*100), 1)
        return percent
    
    def last_change(self):
        string = datetime.datetime.combine(self.last_updated_date, self.last_updated)
        return string
    ##got the list to work now i need to quatify it and just convert to a float

