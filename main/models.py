from django.db import models

# Create your models here.


class Terr(models.Model):
    num = models.IntegerField(default=0)
    sub = models.CharField(max_length=100)
    Owner = models.CharField(max_length=100)
    long_cordinate = models.FloatField(default=0)
    lat_cordinate = models.FloatField(default=0)

    def __str__(self):
        return str(self.num) + ' '+ self.sub + ' ' + self.Owner


class Street(models.Model):
    terr = models.ForeignKey(Terr, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount_numbers = models.IntegerField(default=0)
