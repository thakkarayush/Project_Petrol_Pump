from django.db import models
from creditor.models import creditor_master
from django.urls import reverse
# Create your models here.
class c_payment(models.Model):
    date=models.DateField()
    creditorid=models.ForeignKey(creditor_master,on_delete=models.CASCADE,related_name="payment")
    amount=models.FloatField()
    choice=[("paytm","paytm"),("googlepay","googlepay"),("bank","bank"),("phonepay","phonepay")]
    type=models.CharField(max_length=20,choices=choice)
    bankname=models.CharField(max_length=20,blank=True,null=True)
    chequeno=models.FloatField(null=True,blank=True)
    branchname=models.CharField(max_length=20,blank=True,null=True)
    check_date=models.DateField(blank=True,null=True)
    reference_id=models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return f"{self.creditorid}-{self.amount}"

    def get_absolute_url(self):
        return reverse("cpayment-view")