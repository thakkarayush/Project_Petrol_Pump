from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import nozzel_master
from django.http.response import JsonResponse
from datetime import datetime
from django.db.models import Sum
# Create your views here.
class NewNozzelView(CreateView):
    model = nozzel_master
    fields = '__all__'
#model_form.html

class ListNozzelView(ListView):
    model = nozzel_master
    context_object_name = 'nozzel'
    template_name = 'nozzel/nozzel_master_list.html'
#model_list.html
class UpdateNozzelView(UpdateView):
    model = nozzel_master
    fields = '__all__'

class DeleteNozzelView(DeleteView):
    model = nozzel_master
    success_url = '/nozzel/view'

#model_confirm_delete.html
class DetailNozzelView(DetailView):
    model = nozzel_master

def type_of_nozzel(request,nid):
    type=nozzel_master.objects.get(id=nid).type
    return JsonResponse({"type":type})

def get_creditor_lit_by_nozzel(request,nid):
    noz=nozzel_master.objects.get(id=nid)
    if noz.type.lower()=='petrol':
        data=noz.nozzel.filter(date=datetime.utcnow().date()).aggregate(Sum('petrolinlit'))

    else:
        data=noz.nozzel.filter(date=datetime.utcnow().date()).aggregate(Sum('dieselinlit'))

    return JsonResponse(data)