from django.db import models
from django.urls import reverse

class Terr(models.Model):
    num = models.IntegerField(default=0)
    sub = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)
    lat_cordinate = models.FloatField(default=0)
    long_cordinate = models.FloatField(default=0)

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.num) + ' ' + self.sub + ' ' + self.owner


class Street(models.Model):
    name = models.CharField(max_length=100)
    date_worked = models.DateField(auto_now_add=True)
    terr = models.ForeignKey(Terr, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Number(models.Model):
    value = models.IntegerField(default=0)
    visit1 = models.CharField(max_length=100, blank=True)
    visit2 = models.CharField(max_length=100, blank=True)
    visit3 = models.CharField(max_length=100, blank=True)
    notes = models.CharField(max_length=100, blank=True)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    date_worked = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.value)
