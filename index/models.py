from django.db import models
from accounts.models import *


# Create your models here.

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.doctor.name + " - " + self.patient.name + " - " + str(self.date) + " - " + str(self.time)


class Disposals(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    disease = models.TextField()
    prescription = models.TextField()

