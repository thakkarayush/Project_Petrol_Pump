from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import vehicle
# Create your views here.
class NewVehicleView(CreateView):
    model = vehicle
    fields = '__all__'

#model_form.html

class ListVehicleView(ListView):
    model = vehicle
    context_object_name = 'vehicles'
#model_list.html
class UpdateVehicleView(UpdateView):
    model = vehicle
    fields = '__all__'

class DeleteVehicleView(DeleteView):
    model = vehicle
    success_url = '/vehicle/view'

#model_confirm_delete.html
class DetailVehicleView(DetailView):
    model = vehicle