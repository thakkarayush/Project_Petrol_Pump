from django.db import models
from django.urls import reverse

# Create your models here.
class tank_master(models.Model):
    date=models.DateField()
    petrolbefore=models.FloatField()
    dieselbefore=models.FloatField()
    petrolafter = models.FloatField()
    dieselafter = models.FloatField()
    lostpetrol = models.FloatField()
    lostdiesel = models.FloatField()
    lostpetrolprice = models.FloatField()
    lostdieselprice = models.FloatField()

    def __str__(self):
        return f"petrol({self.lostpetrol})-diesel({self.lostdiesel})"

    def get_absolute_url(self):
        return reverse('Tank-view')