from django.db import models

# Create your models here.

class Appointment(models.Model):
    client_id=models.IntegerField()
    service_id=models.IntegerField()
    scheduled_date=models.DateField()
    status=models.CharField(max_length=50)