from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.getData),
    path('users/xlsx', views.getDataXLSX),
    path('users/add/', views.addUser),
]
