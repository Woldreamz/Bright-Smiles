# Generated by Django 5.1.3 on 2024-11-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_no', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('doctors', models.ManyToManyField(blank=True, related_name='working_in', to='doctors.doctor')),
            ],
        ),
    ]