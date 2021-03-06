from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from nozzel.models import nozzel_master
from datetime import datetime
# Create your models here.
class ntransaction(models.Model):
    date=models.DateField(default=datetime.utcnow)
    nozzelid = models.ForeignKey(nozzel_master, on_delete=models.CASCADE, related_name="payment")
    amount = models.FloatField(blank=True, null=True,default=0)

    bankname = models.CharField(max_length=20, blank=True, null=True)
    branchname = models.CharField(max_length=20, blank=True, null=True)
    cash = models.CharField(max_length=20, blank=True, null=True,default=0)
    totalpetrol=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")],default=0)
    totaldiesel=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")],default=0)
    totalpprice=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")],default=0)
    totaldprice=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")],default=0)
    paytm=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")],default=0)
    googlepay=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")],default=0)
    card = models.FloatField(null=True,blank=True,default=0)
    phonepay = models.FloatField(null=True,blank=True,default=0)
    lostpetrol = models.FloatField(null=True,blank=True,default=0)
    lostdiesel = models.FloatField(null=True,blank=True,default=0)
    lostpetrolprice = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")],default=0)
    lostdieselprice = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")],default=0)
    openingtime=models.TimeField(null=True,blank=True)
    closingtime=models.TimeField(null=True,blank=True)
    openinglitpetrol=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")],default=0)
    closinglitpetrol=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")],default=0)
    openinglitdiesel=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")],default=0)
    closinglitdiesel=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")],default=0)
    creditoramount=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")],default=0)

    def __str__(self):
        return f"{self.nozzelid}-{self.amount}"

    def get_absolute_url(self):
        return reverse('ntransaction-view')