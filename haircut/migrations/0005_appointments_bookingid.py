# Generated by Django 3.2.4 on 2022-01-09 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haircut', '0004_alter_notificationtokens_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='bookingID',
            field=models.PositiveIntegerField(default=12345678),
            preserve_default=False,
        ),
    ]
