"""
URL configuration for hosmag_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospital.views import home, patient_list, doctor_list, appointment_list, add_patient, add_doctor, add_appointment, edit_patient, delete_patient,edit_doctor,delete_doctor,edit_appointment,delete_appointment


urlpatterns = [
    path('',home, name='home'),
    path('patients/', patient_list, name='patient_list'),
    path('doctors/', doctor_list, name='doctor_list'),
    path('appointments/', appointment_list, name='appointment_list'),
    path('add-patient/', add_patient, name='add_patient'),
    path('edit-patient/<int:patient_id>/', edit_patient, name='edit_patient'),
    path('delete-patient/<int:patient_id>/', delete_patient, name='delete_patient'),
    path('add-doctor/', add_doctor, name='add_doctor'),
    path('edit-doctor/<int:doctor_id>/', edit_doctor, name='edit_doctor'),
    path('delete-doctor/<int:doctor_id>/', delete_doctor, name='delete_doctor'),
    path('add-appointment/', add_appointment, name='add_appointment'),
    path(
    'edit-appointment/<int:appointment_id>/',
    edit_appointment,
    name='edit_appointment'
    ),
    path(
    'delete-appointment/<int:appointment_id>/',
    delete_appointment,
    name='delete_appointment'
    ),
    path('admin/', admin.site.urls),
]
