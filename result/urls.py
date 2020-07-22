from django.urls import path
from . import views

urlpatterns = [
    path('', views.result, name='result'),
    path('rank/', views.rank, name='rank'),
]