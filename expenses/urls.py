from django.urls import path
from .views import *

urlpatterns=[
    path('new/',NewExpenseView.as_view(),name="expense-new"),
    path('view/',ListExpenseView.as_view(),name="expense-view"),
    path('update/<int:pk>',UpdateExpenseView.as_view(),name="expense-update"),
    path('delete/<int:pk>',DeleteExpenseView.as_view(),name="expense-delete"),
    path('detail/<int:pk>',DetailExpenseView.as_view(),name="expense-detail")
]