from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import calcmasters
# Create your views here.
class NewcalcmasterView(CreateView):
    model = calcmasters
    fields = '__all__'

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
