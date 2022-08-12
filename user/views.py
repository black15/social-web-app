from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from .models import Profile

# Create your views here.

@login_required
def dashboard_view(request):
   return render(request, 'user/home.html', {'select': 'dashboard'})

def login_view(request):
   if request.user.is_authenticated:
      return redirect('user:dashboard')
   if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():
         cleaned_data = form.cleaned_data
         user = authenticate(
            username=cleaned_data['username'],
            password=cleaned_data['password']
                  )
         try:
            if user.is_active:
               login(request, user)
               return redirect('user:dashboard')
            else:
               return HttpResponse('Login Failed')
         except:
            return HttpResponse('Login Failed')
   else:
      form = LoginForm()
   return render(request, 'user/login.html', {'form': form})

def register_view(request):
   if request.user.is_authenticated:
      return redirect('user:dashboard')
   if request.method == 'POST':
      form = RegisterForm(request.POST)
      if form.is_valid():
         new_user = form.save(commit=False)
         new_user.set_password(
            form.c_password2()
         )
         new_user.save()
         
         # Create profile for the new user
         Profile.objects.create(
            user=new_user
         )
         
         return redirect('user:login')

   else:
      form = RegisterForm()

   return render(request, 'user/register.html', {'form': form})
   