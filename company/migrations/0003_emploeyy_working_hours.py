# Generated by Django 5.1 on 2024-08-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0002_alter_company_adress_alter_company_bio_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="emploeyy",
            name="working_hours",
            field=models.ManyToManyField(to="company.working_hour"),
        ),
    ]
