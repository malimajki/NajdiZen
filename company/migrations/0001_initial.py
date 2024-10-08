# Generated by Django 5.1 on 2024-08-12 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Emploeyy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("phone", models.CharField(max_length=20, null=True)),
                ("bio", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Working_day",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("day", models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("logo", models.ImageField(null=True, upload_to="company_logo")),
                ("bio", models.TextField(null=True)),
                ("adress", models.CharField(max_length=200, null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("phone", models.CharField(max_length=20, null=True)),
                ("www", models.CharField(max_length=200, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("service", models.ManyToManyField(to="company.service")),
            ],
        ),
        migrations.CreateModel(
            name="Working_hour",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time_from", models.TimeField()),
                ("time_to", models.TimeField()),
                (
                    "day",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.working_day",
                    ),
                ),
            ],
        ),
    ]
