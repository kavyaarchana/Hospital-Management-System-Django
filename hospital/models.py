from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=10) 

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete= models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete= models.CASCADE)
    appointment_date = models.DateField()

    def _str_(self):
        return f"{self.patient}-{self.doctor}"
