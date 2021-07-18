from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import calcmasters
from n_transaction.models import ntransaction
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
        ctx["closinglitpetrol"] = ntransaction.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('closinglitpetrol'))['closinglitpetrol__sum']
        ctx["openinglitpetrol"] = ntransaction.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('openinglitpetrol'))['openinglitpetrol__sum']
        ctx["closinglitdiesel"] = ntransaction.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('closinglitdiesel'))['closinglitdiesel__sum']
        ctx["openinglitdiesel"] = ntransaction.objects.filter(date=datetime.utcnow().date()).aggregate(Sum('openinglitdiesel'))['openinglitdiesel__sum']
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