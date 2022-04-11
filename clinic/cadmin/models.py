from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctor_name=models.CharField(max_length=100,unique=True)
    department=models.CharField(max_length=100)
    duty_time=models.TimeField()
    fees=models.IntegerField()

    def __str__(self):
       return self.doctor_name

class Appointment(models.Model):
    doctor_name=models.CharField(max_length=100)
    patient_name=models.CharField(max_length=100)
    sex_options=(
        ("Male","Male"),
        ("Female","Female"),
        ("other","other")
    )
    patient_gender=models.CharField(max_length=100,choices=sex_options)
    patient_phno=models.CharField(max_length=10)
    appointment_date=models.DateField()
    appointment_time=models.TimeField()
    options=(
        ("available","available"),
        ("on-duty","on-duty"),
        ("off-duty","off-duty"))
    status=models.CharField(max_length=100,choices=options,default="available")

