from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import employeepayment
# Create your views here.
class NewemployeepaymentView(CreateView):
    model = employeepayment
    fields = '__all__'
    template_name = "employeepayment/employeepayment_form.html"
#model_form.html

class ListemployeepaymentView(ListView):
    model = employeepayment
    context_object_name = 'employeepayments'
    template_name = "employeepayment/employeepayment_list.html"

#model_list.html
class UpdateemployeepaymentView(UpdateView):
    model = employeepayment
    fields = '__all__'

class DeleteemployeepaymentView(DeleteView):
    model = employeepayment
    success_url = '/employeepayment/view'

#model_confirm_delete.html
class DetailemployeepaymentView(DetailView):
    model = employeepayment