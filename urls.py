from django.urls import path
from . import views

urlpatterns = [
    path('', views.rede_list, name='rede_list'),
    path('rede/new/', views.rede_new, name='rede_new'),
]

