from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from datetime import datetime
# Create your models here.
class calcmasters(models.Model):
    date=models.DateField(default=datetime.utcnow)
    ptank_open=models.FloatField(default=0)
    ptank_close = models.FloatField(default=0)
    dtank_open=models.FloatField(default=0)
    dtank_close = models.FloatField(null=True,blank=True,default=0)
    totalpetrol = models.FloatField(null=True,blank=True,default=0)
    totaldiesel = models.FloatField(null=True,blank=True,default=0)
    lostpetrol = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")],default=0)
    lostdiesel = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")],default=0)

    def __str__(self):
        return f"{self.ptank_close}-{self.dtank_close}"

    def get_absolute_url(self):
        return reverse('calcmaster-view')