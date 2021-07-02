from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
# Create your models here.
class supplierdetails(models.Model):
    date=models.DateField()
    receipt_no=models.IntegerField(validators=[MinValueValidator(0,"Value must be greater than 0")])
    petrolbefore=models.FloatField()
    dieselbefore=models.FloatField()
    time=models.TimeField()
    petrolloss = models.FloatField(null=True,blank=True)
    dieselloss = models.FloatField(null=True,blank=True)
    transportation_in=models.IntegerField(validators=[MinValueValidator(0,"Value must be greater than 0")])
    def __str__(self):
        return f"petrol({self.lostpetrol})-diesel({self.lostdiesel})"
    def get_absolute_url(self):
        return reverse('supplierdetail-view')