from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    medicalLicenseNumber = models.CharField(max_length=100, default="")
    speciality = models.CharField(max_length=100)
    subspeciality = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=100)
    qualification = models.TextField()
    available = models.BooleanField(default=True)
    workplace = models.CharField(max_length=100, default="")
    email = models.EmailField(unique=True)
    contact = models.BigIntegerField()  
    password = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name + " - " + self.speciality


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dateOfBirth = models.DateField(default=datetime.datetime.now())
    dateOfDeath = models.DateField(default=datetime.datetime.now(), null=True)
    gender = models.CharField(max_length=10)  # Male or Female
    address = models.CharField(max_length=200)
    contact = models.BigIntegerField()  # A ten digit number for mobile number
    email = models.EmailField()
    nationality = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name 
    
class Availability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    workDay = models.CharField(max_length=10)
    startTime = models.TimeField()
    endTime = models.TimeField()



   