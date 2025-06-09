from django.urls import path
from . import views

urlpatterns = [
    path('', views.term_list, name='term_list'),
]