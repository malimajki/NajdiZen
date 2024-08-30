from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User

class WorkingDay(models.Model):
    day_of_week = models.IntegerField(choices=[
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()

#Kadernictvi, tetovaci salon, masaze
class ServiceType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

#strihani, holeni, masaz zad, masaz nohou, masaz hlavy, tetovani barevne, tetovani cernobile
class ServiceDetail(models.Model):
    name = models.CharField(max_length=100, unique=True)
    min_price = models.DecimalField(blank=True, null=True)
    max_price = models.DecimalField(blank=True, null=True)

    def __str__(self):
        return self.name

#info about company / service provider
class Business(models.Model):
    service_types = models.ManyToManyField(ServiceType, related_name='businesses')
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    workingday = models.ManyToManyField(WorkingDay)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='employees')
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    services_provided = models.ManyToManyField(ServiceDetail, related_name='employees')
    appointment_duration = models.IntegerField(default=30)

    def __str__(self):
        return f"{self.name} ({self.business})"

    def get_occupied_slots(self, date):
        appointments = self.appointments.filter(date=date)
        occupied_slots = [appointment.time_slot for appointment in appointments]
        return occupied_slots
    

class Calendar(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='calendar')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def get_available_time_slots(self):
        slots = []
        current_time = self.start_time
        while current_time < self.end_time:
            slots.append(current_time)
            if self.employee.appointment_duration == 30:
                current_time = (datetime.combine(datetime.today(), current_time) + timedelta(minutes=30)).time()
            else:
                current_time = (datetime.combine(datetime.today(), current_time) + timedelta(hours=1)).time()
        return slots

    def __str__(self):
        return f"{self.employee.name} - {self.date}"
    

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    time_slot = models.TimeField()

    class Meta:
        unique_together = ('employee', 'date', 'time_slot')

    def __str__(self):
        return f"{self.user.username} - with {self.employee.name} on {self.date} at {self.time_slot}"