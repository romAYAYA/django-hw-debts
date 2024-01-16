from django.urls import path

from django_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_currency/', views.request_currency, name='get_currency'),
    path('create_task/', views.create_task, name='create_task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task')
]
