from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_test:home')
    else:
        form = RegisterForm()
    return render(request, 'register/register.html', {"form": form})

@login_required
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('/login')
    return render(request, 'registration/logout.html')