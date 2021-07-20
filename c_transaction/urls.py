from django.urls import path

from .models import print_page
from .views import *
urlpatterns=[
    path("new/",NewCtransactionView.as_view(),name="ctransaction-new"),
    path("view/",ListCtransactionView.as_view(),name="ctransaction-view"),
    path("update/<int:pk>",UpdateCtransactionView.as_view(),name="ctransaction-update"),
    path("detail/<int:pk>",DetailCtransactionView.as_view(),name="ctransaction-detail"),
    path("delete/<int:pk>",DeleteCtransactionView.as_view(),name="ctransaction-delete"),
    path("print/<int:id>",print_page,name="print-page")
]