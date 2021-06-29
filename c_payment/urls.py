from django.urls import path
from .views import *
urlpatterns=[
    path("new/",NewCpaymentView.as_view(),name="cpayment-new"),
    path("view/",ListCpaymentView.as_view(),name="cpayment-view"),
    path("update/<int:pk>",UpdateCpaymentView.as_view(),name="cpayment-update"),
    path("delete/<int:pk>",DeleteCpaymentView.as_view(),name="cpayment-delete"),
    path("detail/<int:pk>",DetailCpaymentView.as_view(),name="cpayment-detail")
]