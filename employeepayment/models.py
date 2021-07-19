from django.db import models
from employee.models import employee
from django.urls import reverse
from datetime import datetime
# Create your models here.
class employeepayment(models.Model):
    date=models.DateField(default=datetime.utcnow)
    employeeid=models.ForeignKey(employee,on_delete=models.CASCADE,related_name="payment")
    amount=models.FloatField()
    finalisesalary=models.FloatField()
    choice=[("paytm","paytm"),("googlepay","googlepay"),("bank","bank"),("phonepay","phonepay"),("cash","cash")]
    type=models.CharField(max_length=20,choices=choice)
    bankname=models.CharField(max_length=20,blank=True,null=True)
    chequeno=models.FloatField(null=True,blank=True)
    branchname=models.CharField(max_length=20,blank=True,null=True)
    cheque_date=models.DateField(blank=True,null=True)
    IFSC=models.IntegerField(null=True,blank=True)
    reference_id=models.CharField(max_length=20,blank=True,null=True)
    remarks=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f"{self.employeeid}-{self.amount}"

    def get_absolute_url(self):
        return reverse("employeepayment-view")