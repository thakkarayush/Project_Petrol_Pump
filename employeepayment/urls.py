from django.urls import path
from .views import *
urlpatterns=[
    path("new/",NewemployeepaymentView.as_view(),name="employeepayment-new"),
    path("view/",ListemployeepaymentView.as_view(),name="employeepayment-view"),
    path("update/<int:pk>",UpdateemployeepaymentView.as_view(),name="employeepayment-update"),
    path("delete/<int:pk>",DeleteemployeepaymentView.as_view(),name="employeepayment-delete"),
    path("detail/<int:pk>",DetailemployeepaymentView.as_view(),name="employeepayment-detail")
]