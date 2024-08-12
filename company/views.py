from django.shortcuts import render
from company.models import Company, Emploeyy

def home(request):
    companies = Company.objects.all()
    employees = Emploeyy.objects.all()

    context = {
        "companies":companies,
        "employees":employees,
    }

    return  render (request, "company/home.html", context)