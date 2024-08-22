from django.shortcuts import render, redirect
from .forms import registerForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have registered successfuly.")
            return redirect('index')
    else:
        form = registerForm()
        return render(request, 'users/register.html', {'form':form})