from django.urls import path

from django_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_currency/', views.request_currency, name='get_currency')
]
