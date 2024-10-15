from django.db import models

# Create your models here.
class Contact(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.username
    

class Car(models.Model):
    car_name = models.CharField(max_length=30)
    speed = models.IntegerField(default=50)

    def __str__(self):
        return self.car_name

