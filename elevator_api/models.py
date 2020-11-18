from django.db import models 


class Elevator(models.Model):
    number = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    ir = models.IntegerField(default=0)
    acceleration_x = models.FloatField(default=0.)
    acceleration_y = models.FloatField(default=0.)
    acceleration_z = models.FloatField(default=0.)
    roll = models.FloatField(default=0.)
    pitch = models.FloatField(default=0.)
    yaw = models.FloatField(default=0.)
    base_altitude = models.FloatField(default=0.)
    current_altitude = models.FloatField(default=0.)
    height = models.FloatField(default=0.)
    permission_number = models.IntegerField(default=0)

    def __str__(self):
        return self.number

class Address(models.Model):
    number = models.IntegerField(default=0, primary_key=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address

class User(models.Model):
    my_id = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    permission_number = models.IntegerField(default=0)
    agency = models.CharField(max_length=100, default='None')

    def __str__(self):
        return self.my_id

#auto_now_add = create date(Can`t change)
#auto_now = update date(change)