# Generated by Django 5.1 on 2024-08-30 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                (
                    "monday_start",
                    models.TimeField(
                        blank=True, default=datetime.time(10, 30), null=True
                    ),
                ),
                (
                    "monday_end",
                    models.TimeField(
                        blank=True, default=datetime.time(14, 30), null=True
                    ),
                ),
                (
                    "tuesday_start",
                    models.TimeField(
                        blank=True, default=datetime.time(8, 30), null=True
                    ),
                ),
                (
                    "tuesday_end",
                    models.TimeField(
                        blank=True, default=datetime.time(14, 30), null=True
                    ),
                ),
                (
                    "wednesday_start",
                    models.TimeField(
                        blank=True, default=datetime.time(8, 30), null=True
                    ),
                ),
                (
                    "wednesday_end",
                    models.TimeField(
                        blank=True, default=datetime.time(14, 30), null=True
                    ),
                ),
                (
                    "thursday_start",
                    models.TimeField(
                        blank=True, default=datetime.time(8, 30), null=True
                    ),
                ),
                (
                    "thursday_end",
                    models.TimeField(
                        blank=True, default=datetime.time(14, 30), null=True
                    ),
                ),
                (
                    "friday_start",
                    models.TimeField(
                        blank=True, default=datetime.time(8, 30), null=True
                    ),
                ),
                (
                    "friday_end",
                    models.TimeField(
                        blank=True, default=datetime.time(14, 30), null=True
                    ),
                ),
                (
                    "saturday_start",
                    models.TimeField(
                        blank=True, default=datetime.time(8, 30), null=True
                    ),
                ),
                (
                    "saturday_end",
                    models.TimeField(
                        blank=True, default=datetime.time(14, 30), null=True
                    ),
                ),
                (
                    "sunday_start",
                    models.TimeField(
                        blank=True, default=datetime.time(8, 30), null=True
                    ),
                ),
                (
                    "sunday_end",
                    models.TimeField(
                        blank=True, default=datetime.time(14, 30), null=True
                    ),
                ),
                (
                    "pausa_start",
                    models.TimeField(
                        blank=True, default=datetime.time(12, 0), null=True
                    ),
                ),
                (
                    "pausa_end",
                    models.TimeField(
                        blank=True, default=datetime.time(13, 0), null=True
                    ),
                ),
                ("slot_duration", models.IntegerField(default=60)),
            ],
        ),
    ]
