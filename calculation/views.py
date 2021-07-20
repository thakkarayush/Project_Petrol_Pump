from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import calcmasters
from n_transaction.models import ntransaction
from tank.models import tank_master
from django.db.models import Sum
from datetime import datetime
# Create your views here.
class NewcalcmasterView(CreateView):
    model = calcmasters
    fields = '__all__'


    def get_context_data(self, **kwargs):
        ctx = super(NewcalcmasterView, self).get_context_data(**kwargs)
        ctx["totalpetrol"] = ntransaction.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('totalpetrol'))['totalpetrol__sum']
        ctx["totaldiesel"] = ntransaction.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('totaldiesel'))['totaldiesel__sum']
        ctx["closinglitpetrol"] = tank_master.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('petrolafter'))['petrolafter__sum']
        ctx["openinglitpetrol"] = tank_master.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('petrolbefore'))['petrolbefore__sum']
        ctx["closinglitdiesel"] = tank_master.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('dieselafter'))['dieselafter__sum']
        ctx["openinglitdiesel"] = tank_master.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('dieselbefore'))['dieselbefore__sum']
        ctx["lostpetrol"] = ntransaction.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('lostpetrol'))['lostpetrol__sum']
        ctx["lostdiesel"] = ntransaction.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('lostdiesel'))['lostdiesel__sum']
        return ctx

#model_form.html

class ListcalcmasterView(ListView):
    model = calcmasters
    context_object_name = 'calcmasters'
#model_list.html
class UpdatecalcmasterView(UpdateView):
    model = calcmasters
    fields = '__all__'

class DeletecalcmasterView(DeleteView):
    model = calcmasters
    success_url = '/calcmaster/view'
#model_confirm_delete.html
class DetailcalcmasterView(DetailView):
    model = calcmasters


# def data(request):
#     data = ntransaction.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('totalpetrol'))
#     print(data)
#     return render(request,'calculation/calcmasters_form.html',{
#         "totalpetrol":data['totalpetrol__sum']
#
#     })