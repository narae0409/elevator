from django.db import models 

class Data(models.Model): 
    time = models.DateTimeField(auto_now_add=True)
    sensor = models.CharField(max_length=30)
    measure = models.IntegerField()
    
    def __str__(self): 
        return self.sensor


class Elevator(models.Model):
    number = models.IntegerField(max_length=7, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    acceleration = models.IntegerField(default=0)
    altitude = models.IntegerField(default=0)

    def __str__(self):
        return self.number