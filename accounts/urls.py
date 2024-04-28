# urls for individual views function inside this app
# """
from django.urls import path, include
from .import views

urlpatterns = [
    path('registerDoctor',views.registerDoctor,name='registerDoctor'),
    path('registerPatient',views.registerPatient,name='registerPatient'),
    path('login',views.loginUser,name='login'),
    path('logout',views.logoutUser,name='logout'),
    
]