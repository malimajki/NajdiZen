from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Company(models.Model):
    service = models.ManyToManyField(Service)
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='company_logo', blank=True)
    bio = models.TextField(blank=True)
    adress = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    www = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Emploeyy(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    working_hours = models.ManyToManyField("Working_hour")

    def __str__(self):
        return self.name
    
class Working_day(models.Model):
    day = models.CharField(max_length=2)

    def __str__(self):
        return self.day

class Working_hour(models.Model):
    day = models.ForeignKey(Working_day, on_delete=models.CASCADE)
    time_from = models.TimeField(auto_now=False, auto_now_add=False)
    time_to = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.day} - {self.time_from} - {self.time_to}"