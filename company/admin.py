from django.contrib import admin
from company.models import Company, Emploeyy, Working_day, Working_hour, Service


admin.site.register(Company)
admin.site.register(Service)
admin.site.register(Emploeyy)
admin.site.register(Working_day)
admin.site.register(Working_hour)