from django.shortcuts import render
from django.db import connection
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .models import *

def registerDoctor(request):
    cursor = connection.cursor()
    if request.method == "POST":
        name = request.POST['name']
        medicalLicenseNumber = request.POST['medicalLicenseNumber']
        speciality = request.POST['speciality']
        subspeciality = request.POST['subspeciality']
        department = request.POST['department']
        qualification = request.POST['qualification']
        workplace = request.POST['workplace']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        
        # Create a new user instance for the doctor
        user = User.objects.create_user(username=email, password=password)
        user_id = user.id
        userUpdateQuery = "UPDATE auth_user SET first_name=%s, last_name=%s, email=%s WHERE username=%s"
        cursor.execute(userUpdateQuery, [name.split(" ")[0], name.split(" ")[1], email, email])
        doctorInsertQuery = """
            INSERT INTO accounts_doctor(user_id, name, medicalLicenseNumber, speciality, subspeciality, department, qualification, workplace, email, contact, password) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(doctorInsertQuery, [user_id, name, medicalLicenseNumber, speciality, subspeciality, department, qualification, workplace, email, contact, password])
    return render(request, 'registerDoctor.html')



def registerPatient(request):
    cursor = connection.cursor()
    if request.method == "POST":
        name = request.POST['name']
        dateOfBirth = request.POST['dateOfBirth']
        gender = request.POST['gender']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']

        # Check if patient with the same email already exists
        patientQuery = "SELECT * FROM accounts_patient WHERE email = %s"
        cursor.execute(patientQuery, [email])
        results = cursor.fetchall()
        if len(results) > 0:
            return render(request, 'registerPatient.html', {'error': 'Patient with this email already exists'})
        else:
            # Create a new user instance for the patient
            hashed_password = make_password(password)
            userInsertQuery = "INSERT INTO auth_user(username, password) VALUES (%s, %s)"
            cursor.execute(userInsertQuery, [email, hashed_password])
            user_id = cursor.lastrowid

            # Insert data into accounts_patient table
            patientInsertQuery = """
                INSERT INTO accounts_patient(user_id, name, dateOfBirth, gender, address, contact, email, password) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(patientInsertQuery, [user_id, name, dateOfBirth, gender, address, contact, email, password])

    return render(request, 'registerPatient.html')


def loginUser(request):
    cursor = connection.cursor()
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Login the user
            login(request, user)
            nameFetchQueryPatient = "SELECT name FROM accounts_patient WHERE email = %s"
            nameFetchQueryDoctor = "SELECT name FROM accounts_doctor WHERE email = %s"

            cursor.execute(nameFetchQueryPatient, [email])
            data = cursor.fetchone()
            if data is None:
                cursor.execute(nameFetchQueryDoctor, [email])
                data = cursor.fetchone()
            
            messages.success(request, 'Successfully logged in, ' + data[0] + '!')
            return redirect("/")
        else:
            messages.error(request, 'Incorrect Email or Password')
            return render(request, 'login.html')
    return render(request, 'login.html')

def loginUser2(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Hash the password
        hashed_password = make_password(password)

        # Authenticate the user using raw SQL query
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM auth_user WHERE username = %s", [email])
            user_data = cursor.fetchone()
            print(user_data)
            if user_data is not None:
                # Check if the hashed password matches
                if check_password(password, user_data[1]):
                    # If the passwords match, log in the user
                    user_id = user_data[0]
                    cursor.execute("UPDATE auth_user SET last_login = NOW() WHERE id = %s", [user_id])
                    
                    # Convert the user_data tuple to a User object
                    user = User.objects.get(id=user_id)
                    
                    login(request, user)
                    messages.success(request, 'Successfully logged in, ' + user.username + '!')
                    return redirect("/")
                else:
                    messages.error(request, 'Incorrect Email or Password')
                    return render(request, 'login.html')
            else:
                messages.error(request, 'User with this email does not exist')
                return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/")
    
