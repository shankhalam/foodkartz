from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import items
from .forms import addItemForm
from .forms import addItemForm


# Create your views here.

item_list = items.objects.all()

def index(request):
    context = {
        'item_list' : item_list,
    }
    return render (request, 'food/index.html', context)

def products(request):
    context = {
        'item_list': item_list
    }
    return render(request, 'food/products.html', context)


def details(request, item_id):
    item = items.objects.get(pk=item_id)
    context = {
        'item' : item,
    }
    return render(request, 'food/detail.html', context)

def createItem(request):
    if request.method == 'POST':
        form = addItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = addItemForm()
    dict_form = {
        'form' : form
    }
    return render(request, 'food/additem.html', dict_form)
