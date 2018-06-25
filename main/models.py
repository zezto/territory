from django.db import models

# Create your models here.


"""class Terr(models.Model):
    num = models.IntegerField(default=0)
    sub = models.CharField(max_length=100)
    Owner = models.CharField(max_length=100)
    long_cordinate = models.FloatField(default=0)
    lat_cordinate = models.FloatField(default=0)

    def __str__(self):
        return str(self.num) + ' ' + self.sub + ' ' + self.Owner


class Street(models.Model):
    terr = models.ForeignKey(Terr, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount_numbers = models.IntegerField(default=0)
    date_worked = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Number(models.Model):
    terr = models.ForeignKey(Terr, on_delete=models.CASCADE, default=0)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    visit1 = models.CharField(max_length=100, blank=True)
    visit2 = models.CharField(max_length=100, blank=True)
    visit3 = models.CharField(max_length=100, blank=True)
    notes = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.value)"""

'''
class Number(models.Model):
    value = models.IntegerField(default=0)
    visit1 = models.CharField(max_length=100, blank=True)
    visit2 = models.CharField(max_length=100, blank=True)
    visit3 = models.CharField(max_length=100, blank=True)
    notes = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.value)


class Street(models.Model):
    name = models.CharField(max_length=100)
    date_worked = models.DateField(auto_now=True)
    numbers = models.ManyToManyField(Number, through='Terr')


    def __str__(self):
        return self.name

class Terr(models.Model):
    houses = models.ForeignKey(Number, on_delete=models.CASCADE, default=0)
    street = models.ForeignKey(Street, on_delete=models.CASCADE, default=0)
    num = models.IntegerField(default=0)
    sub = models.CharField(max_length=100)
    Owner = models.CharField(max_length=100)
    lat_cordinate = models.FloatField(default=0)
    long_cordinate = models.FloatField(default=0)

    def __str__(self):
        return str(self.num) + ' ' + self.sub + ' ' + self.Owner

        #try many to one relationship now lol 
        #also try rverse relation too accoridn to your stackoverflow
        #many to one now lol
'''
class Terr(models.Model):
    num = models.IntegerField(default=0)
    sub = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    lat_cordinate = models.FloatField(default=0)
    long_cordinate = models.FloatField(default=0)

    def __str__(self):
        return str(self.num) + ' ' + self.sub + ' ' + self.owner

class Street(models.Model):
    name = models.CharField(max_length=100)
    date_worked = models.DateField(auto_now=True)
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

    def __str__(self):
        return str(self.value)
