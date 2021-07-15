from django.db import models
from creditor.models import  creditor_master
from django.urls import reverse
from datetime import datetime
# Create your models here.
class vehicle(models.Model):
    date=models.DateField(default=datetime.utcnow)
    v_no=models.CharField(max_length=20)
    driver_name=models.CharField(max_length=25,null=True,blank=True)
    choices=[("petrol","petrol"),("diesel","diesel")]
    fuel_type=models.CharField(max_length=10,choices=choices)
    remarks=models.CharField(max_length=40)
    creditor=models.ForeignKey(creditor_master,on_delete=models.CASCADE,related_name='vehicle')

    def __str__(self):
        return f"{self.v_no}"

    def get_absolute_url(self):
        return reverse('vehicle-view')
