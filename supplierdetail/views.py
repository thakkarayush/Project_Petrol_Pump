from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import supplierdetails
# Create your views here.
class NewsupplierdetailView(CreateView):
    model = supplierdetails
    fields = '__all__'
#model_form.html
class ListsupplierdetailView(ListView):
    model = supplierdetails
    context_object_name = 'supplierdetails'
#model_list.html
class UpdatesupplierdetailView(UpdateView):
    model = supplierdetails
    fields = '__all__'
class DeletesupplierdetailView(DeleteView):
    model = supplierdetails
    success_url = '/supplierdetail/view'
#model_confirm_delete.html
class DetailsupplierdetailView(DetailView):
    model = supplierdetails