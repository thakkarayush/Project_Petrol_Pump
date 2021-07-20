from django.db.models.functions import TruncMonth
from django.shortcuts import render
from tank.models import tank_master
from datetime import datetime
from creditor.models import creditor_master
from django.db.models import Sum
from n_transaction.models import ntransaction
from django.http.response import JsonResponse
from rates.models import rate
# Create your views here.
def home(request):
    return render(request,"user/home.html")

def dashboard(request):
    today=tank_master.objects.get(date=datetime.utcnow().date());
    petrol_stock=today.petrolafter
    diesel_stock = today.dieselafter

    #creditor amount
    data = creditor_master.objects.all().aggregate(Sum('pendingbalance'))
    print(data)

    #todays Earning
    data1=ntransaction.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('amount'))
    print(data)

    return render(request,'user/dashboard.html',{
        "petrol_stock":petrol_stock,
        "diesel_stock":diesel_stock,
        'pending_amount':data['pendingbalance__sum'],
        'earning':data1['amount__sum']
    })

def get_petrol_amount_by_month_chart(request):
    from django.db.models import Sum
    from datetime import datetime
    from calculation.models import calcmasters
    result = calcmasters.objects.annotate(month=TruncMonth('date')).values('month').annotate(
         no_of_ad=Sum('totalpetrol'))
    data = {'label': [], 'values': []}
    for ex in result:
        data['label'].append(datetime.strftime(ex['month'], '%B'))
        data['values'].append(ex['no_of_ad'])
        print(data)
    return JsonResponse(data)

def get_diesel_amount_by_month_chart(request):
    from django.db.models import Sum
    from datetime import datetime
    from calculation.models import calcmasters
    result = calcmasters.objects.annotate(month=TruncMonth('date')).values('month').annotate(
        no_of_ad1=Sum('totaldiesel'))
    data1 = {'label': [], 'values': []}
    for ex in result:
        data1['label'].append(datetime.strftime(ex['month'], '%B'))
        data1['values'].append(ex['no_of_ad1'])
        print(data1)
    return JsonResponse(data1)