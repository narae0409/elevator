from django.db import models 

class Data(models.Model): 
    time = models.DateTimeField(auto_now_add=True)
    sensor = models.CharField(max_length=30)
    measure = models.IntegerField()
    
    def __str__(self): 
        return self.sensor
