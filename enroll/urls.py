from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("view_emp", views.view),
    path("add_emp", views.add),
    path("remove_emp", views.remove),
    path("filter_emp", views.filter),
]
