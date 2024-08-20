from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('<int:item_id>/', views.details, name='details'),
    path('additem/', views.createItem, name='additem'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item')
]