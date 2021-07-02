from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import ntransaction
# Create your views here.
class NewCtransactionView(CreateView):
    model = ntransaction
    fields = '__all__'

#model_form.html

class ListCtransactionView(ListView):
    model = ntransaction
    context_object_name = 'ntransactions'
#model_list.html
class UpdateCtransactionView(UpdateView):
    model = ntransaction
    fields = '__all__'

class DeleteCtransactionView(DeleteView):
    model = ntransaction
    success_url = '/ntransaction/view'
#model_confirm_delete.html
class DetailCtransactionView(DetailView):
    model = ntransaction

