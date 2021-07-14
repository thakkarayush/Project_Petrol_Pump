from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from datetime import datetime
# Create your models here.
class calcmasters(models.Model):
    date=models.DateField(default=datetime.utcnow)
    ptank_open=models.FloatField()
    ptank_close = models.FloatField()
    dtank_open=models.FloatField()
    dtank_close = models.FloatField(null=True,blank=True)
    totalpetrol = models.FloatField(null=True,blank=True)
    totaldiesel = models.FloatField(null=True,blank=True)
    lostpetrol = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])
    lostdiesel = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])

    def __str__(self):
        return f"petrol({self.lostpetrol})-diesel({self.lostdiesel})"

    def get_absolute_url(self):
        return reverse('calcmaster-view')