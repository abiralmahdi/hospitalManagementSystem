from django.shortcuts import render
import datetime
from accounts.models import Doctor, Patient
from .models import Appointment
from django.db import connection
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'index.html')


def makeAppointment(request):
    cursor = connection.cursor()
    if request.method == "POST":
        doctorID = request.POST['doctor']
        doctorQuery = "SELECT * FROM accounts_doctor WHERE id = %s"
        cursor.execute(doctorQuery, [doctorID])

        patientID = request.user.id
        patientQuery = "SELECT * FROM accounts_patient WHERE user_id = %s"
        cursor.execute(patientQuery, [patientID])

        date = datetime.datetime.now().strftime('%Y-%m-%d')
        time = datetime.datetime.now().strftime('%H:%M:%S')

        insertQuery = "INSERT INTO index_appointment(doctor_id, patient_id, date, time) VALUES (%s, %s, %s, %s)"
        cursor.execute(insertQuery, [doctorID, patientID, date, time])

    return render(request, 'makeAppointment.html')


