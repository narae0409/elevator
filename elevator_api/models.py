from django.db import models 


class Elevator(models.Model):
    number = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    acceleration = models.IntegerField(default=0)
    altitude = models.IntegerField(default=0)
    pir = models.BooleanField(default=False)

    def __str__(self):
        return self.number

class Address(models.Model):
    number = models.IntegerField(default=0, primary_key=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address

#auto_now_add = create date(Can`t change)
#auto_now = update date(change)