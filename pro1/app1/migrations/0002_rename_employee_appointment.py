# Generated by Django 5.1.4 on 2024-12-10 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Appointment',
        ),
    ]
