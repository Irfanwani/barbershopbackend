# Generated by Django 4.0.3 on 2022-04-10 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haircut', '0006_appointments_services_appointments_totalcost'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
