#from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class owner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class pet(models.Model):
    Male='M'
    Female='F'
    pet_gender_choices=[
        (Male,'M'),
        (Female,'F')
    ]
    
    pet_type = models.CharField(max_length=200)
    pet_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender= models.CharField(max_length=1, choices=pet_gender_choices)
    owner = models.ForeignKey(owner, on_delete=models.CASCADE)
    description =  models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pet_type + ", " + self.pet_name
         



