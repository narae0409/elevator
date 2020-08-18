from django.db import models 

class Data(models.Model): 
    sensor = models.CharField(max_length=30)
    measure = models.IntegerField()
    
    def __str__(self): 
        return self.sensor