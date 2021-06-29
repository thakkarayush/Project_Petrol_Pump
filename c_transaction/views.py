from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import c_transaction
# Create your views here.
class NewCtransactionView(CreateView):
    model = c_transaction
    fields = '__all__'

#model_form.html

class ListCtransactionView(ListView):
    model = c_transaction
    context_object_name = 'Ctransactions'
#model_list.html
class UpdateCtransactionView(UpdateView):
    model = c_transaction
    fields = '__all__'

class DeleteCtransactionView(DeleteView):
    model = c_transaction
    success_url = '/c_transaction/view'
#model_confirm_delete.html
class DetailCtransactionView(DetailView):
    model = c_transaction