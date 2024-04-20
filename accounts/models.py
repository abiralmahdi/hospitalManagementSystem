from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    qualification = models.TextField()
    email = models.EmailField(unique=True)
    contact = models.BigIntegerField()  # A ten digit number for mobile number

    def __str__(self):
        return self.name + " - " + self.speciality


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=10)  # Male or Female
    address = models.CharField(max_length=200)
    contact = models.BigIntegerField()  # A ten digit number for mobile number
    email = models.EmailField()

    def __str__(self):
        return self.name 
