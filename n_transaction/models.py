from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from nozzel.models import nozzel_master

# Create your models here.
class ntransaction(models.Model):
    date=models.DateField()
    nozzelid = models.ForeignKey(nozzel_master, on_delete=models.CASCADE, related_name="payment")
    amount = models.FloatField()
    choice = [("paytm", "paytm"), ("googlepay", "googlepay"), ("bank", "bank"), ("phonepay", "phonepay"),
              ("cash", "cash")]
    type = models.CharField(max_length=20, choices=choice)
    bankname = models.CharField(max_length=20, blank=True, null=True)
    branchname = models.CharField(max_length=20, blank=True, null=True)
    reference_id = models.CharField(max_length=20, blank=True, null=True)
    totalpetrol=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])
    totaldiesel=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])
    totalpprice=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])
    totaldprice=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])
    petrolbefore=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])
    dieselbefore=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])
    petrolafter = models.FloatField(null=True,blank=True)
    dieselafter = models.FloatField(null=True,blank=True)
    lostpetrol = models.FloatField(null=True,blank=True)
    lostdiesel = models.FloatField(null=True,blank=True)
    lostpetrolprice = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])
    lostdieselprice = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])
    openingtime=models.FloatField()
    closingtime=models.FloatField()
    openinglitpetrol=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])
    closinglitpetrol=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])
    openinglitdiesel=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])
    closinglitdiesel=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])
    creditorslipno=models.FloatField(null=True,blank=True,validators=[MinValueValidator(0,"Value must be greater than 0")])

    def __str__(self):
        return f"petrol({self.lostpetrol})-diesel({self.lostdiesel})"

    def get_absolute_url(self):
        return reverse('ntransaction-view')