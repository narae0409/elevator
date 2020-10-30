from django.db import models 


class Elevator(models.Model):
    number = models.IntegerField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    acceleration = models.IntegerField(default=0)
    altitude = models.IntegerField(default=0)

    def __str__(self):
        return self.number