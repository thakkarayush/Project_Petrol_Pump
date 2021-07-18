from django.urls import path
from nozzel.views import *
urlpatterns=[
    path("entry/",NewNozzelView.as_view(),name="nozzel-entry"),
    path("view/",ListNozzelView.as_view(),name="nozzel-view"),
    path("update/<int:pk>",UpdateNozzelView.as_view(),name="nozzel-update"),
    path("delete/<int:pk>",DeleteNozzelView.as_view(),name="nozzel-delete"),
    path("detail/<int:pk>",DetailNozzelView.as_view(),name="nozzel-detail"),
    path("type/<int:nid>",type_of_nozzel,name='nozzel-type'),
    path("camount/<int:nid>",get_creditor_lit_by_nozzel,name='creditor-amount')
]