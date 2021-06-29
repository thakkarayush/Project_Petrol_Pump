from django.db import models
from django.urls import reverse
from vehicle.models import vehicle
from nozzel.models import nozzel_master
# Create your models here.

class c_transaction(models.Model):
    date=models.DateField()
    vehicle_id=models.ForeignKey(vehicle,on_delete=models.CASCADE,related_name='ctransaction')
    petrolinlit=models.FloatField(null=True,blank=True)
    dieselinlit=models.FloatField(null=True,blank=True)
    petrolprice=models.FloatField(null=True,blank=True)
    dieselprice=models.FloatField(null=True,blank=True)
    nozzel=models.ForeignKey(nozzel_master, on_delete=models.CASCADE, related_name='nozzel')

    def __str__(self):
        return f"petrol({self.date})-diesel({self.vehicle_id})"

    def get_absolute_url(self):
        return reverse('ctransaction-view')