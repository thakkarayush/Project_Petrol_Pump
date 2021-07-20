from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from .models import expense
# Create your views here.

class NewExpenseView(CreateView):
    model = expense
    fields = '__all__'

class ListExpenseView(ListView):
    model = expense
    context_object_name = 'expense'

class DeleteExpenseView(DeleteView):
    model = expense
    success_url = '/expense/view'

class UpdateExpenseView(UpdateView):
    model = expense
    fields = '__all__'

class DetailExpenseView(DetailView):
    model = expense
    success_url = '/expense/view'