# Generated by Django 5.1.3 on 2024-11-11 08:49

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0002_rename_phone_no_clinic_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]