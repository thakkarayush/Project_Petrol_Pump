from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import c_payment
# Create your views here.
class NewCpaymentView(CreateView):
    model = c_payment
    fields = '__all__'

#model_form.html

class ListCpaymentView(ListView):
    model = c_payment
    context_object_name = 'cpayments'
#model_list.html
class UpdateCpaymentView(UpdateView):
    model = c_payment
    fields = '__all__'

class DeleteCpaymentView(DeleteView):
    model = c_payment
    success_url = '/c_payment/view'

#model_confirm_delete.html
class DetailCpaymentView(DetailView):
    model = c_payment