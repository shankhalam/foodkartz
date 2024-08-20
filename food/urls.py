from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('<int:item_id>/', views.details, name='details'),
    path('additem/', views.createItem, name='additem'),
]