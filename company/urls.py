from django.urls import path
from company.views import home

app_name = "company"

urlpatterns = [
    path("", home, name="home"),
]
