from django.shortcuts import render, redirect
from .models import Employee
from datetime import datetime, timedelta

def index(request):
    zamestanci = Employee.objects.all()

    return render (request, 'index.html', {"zamestanci":zamestanci})