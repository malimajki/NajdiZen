from django.db import models
from datetime import timedelta, time, datetime

class Employee(models.Model):
    name = models.CharField(max_length=100)

    monday_start = models.TimeField(blank=True, null=True, default=time(10, 30))
    monday_end = models.TimeField(blank=True, null=True, default=time(14, 30))
    tuesday_start = models.TimeField(blank=True, null=True, default=time(8, 30))
    tuesday_end = models.TimeField(blank=True, null=True, default=time(14, 30))
    wednesday_start = models.TimeField(blank=True, null=True, default=time(8, 30))
    wednesday_end = models.TimeField(blank=True, null=True, default=time(14, 30))
    thursday_start = models.TimeField(blank=True, null=True, default=time(8, 30))
    thursday_end = models.TimeField(blank=True, null=True, default=time(14, 30))
    friday_start = models.TimeField(blank=True, null=True, default=time(8, 30))
    friday_end = models.TimeField(blank=True, null=True, default=time(14, 30))

    saturday_start = models.TimeField(blank=True, null=True, default=time(8, 30))
    saturday_end = models.TimeField(blank=True, null=True, default=time(14, 30))
    sunday_start = models.TimeField(blank=True, null=True, default=time(8, 30))
    sunday_end = models.TimeField(blank=True, null=True, default=time(14, 30))

    pausa_start = models.TimeField(blank=True, null=True, default=time(12, 00))
    pausa_end = models.TimeField(blank=True, null=True, default=time(13, 00))

    slot_duration = models.IntegerField(default=60)

    def __str__(self):
        return self.name

    def get_monday_slots(self):
        monday_slots = []
        time = self.monday_start
        while time < self.monday_end:
            if time >= self.pausa_start and time <= self.pausa_end:
                pass
            else:
                monday_slots.append(time.strftime("%H:%M"))
            time = (datetime.combine(datetime.today(), time) + timedelta(minutes=self.slot_duration)).time()
        return monday_slots
    
    def get_tuesday_slots(self):
        tuesday_slots = []
        time = self.tuesday_start
        while time < self.tuesday_end:
            if time >= self.pausa_start and time <= self.pausa_end:
                pass
            else:
                tuesday_slots.append(time.strftime("%H:%M"))
            time = (datetime.combine(datetime.today(), time) + timedelta(minutes=self.slot_duration)).time()
        return tuesday_slots
    
    def get_wednesday_slots(self):
        wednesday_slots = []
        time = self.wednesday_start
        while time < self.wednesday_end:
            if time >= self.pausa_start and time <= self.pausa_end:
                pass
            else:
                wednesday_slots.append(time.strftime("%H:%M"))
            time = (datetime.combine(datetime.today(), time) + timedelta(minutes=self.slot_duration)).time()
        return wednesday_slots
    
    def get_thursday_slots(self):
        thursday_slots = []
        time = self.thursday_start
        while time < self.thursday_end:
            if time >= self.pausa_start and time <= self.pausa_end:
                pass
            else:
                thursday_slots.append(time.strftime("%H:%M"))
            time = (datetime.combine(datetime.today(), time) + timedelta(minutes=self.slot_duration)).time()
        return thursday_slots
    
    def get_friday_slots(self):
        friday_slots = []
        time = self.friday_start
        while time < self.friday_end:
            if time >= self.pausa_start and time <= self.pausa_end:
                pass
            else:
                friday_slots.append(time.strftime("%H:%M"))
            time = (datetime.combine(datetime.today(), time) + timedelta(minutes=self.slot_duration)).time()
        return friday_slots
    
    def get_saturday_slots(self):
        saturday_slots = []
        time = self.saturday_start
        while time < self.saturday_end:
            if time >= self.pausa_start and time <= self.pausa_end:
                pass
            else:
                saturday_slots.append(time.strftime("%H:%M"))
            time = (datetime.combine(datetime.today(), time) + timedelta(minutes=self.slot_duration)).time()
        return saturday_slots
    
    def get_sunday_slots(self):
        sunday_slots = []
        time = self.sunday_start
        while time < self.sunday_end:
            if time >= self.pausa_start and time <= self.pausa_end:
                pass
            else:
                sunday_slots.append(time.strftime("%H:%M"))
            time = (datetime.combine(datetime.today(), time) + timedelta(minutes=self.slot_duration)).time()
        return sunday_slots