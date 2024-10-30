from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginRequiredView(LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'redirect_to'

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('birthday_view')
            else:
                print("Incorrect creds")
                return render(request, 'login.html', {'form': form, "error": "Incorrect credentials"})
        else:
            return render(request, 'login.html', {'form': form, "error": "Invalid form"})
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, "message": "You have been logged out."})
