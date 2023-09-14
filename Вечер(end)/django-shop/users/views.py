from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from django.contrib import messages


def register_view(request):
    if request.method == 'POST': # является ли запрос POST
        form = RegisterForm(request.POST) # если да, то валидирует форму регистрации.
        if form.is_valid(): # Если форма валидна
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save() # то функция сохраняет пользователя, используя введенные данные
            messages.success(request, 'Account created successfully')
            return redirect('login') # и перенаправляет пользователя на страницу входа.
    else: # Если запрос не является POST, то функция просто отображает форму входа.
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST': # Функция проверяет, является ли запрос POST
        form = LoginForm(request=request, data=request.POST) # если да, то валидирует форму входа.
        if form.is_valid(): # Если форма валидна 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password) # функция аутентифицирует пользователя
            if user is not None: # если пользователь существует
                login(request, user) #  сохраняет его сеанс 
                return redirect('home') # перенаправляет на страницу home
    else: # Если запрос не является POST, то функция просто отображает форму входа.
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def home_view(request):
    return render(request, 'home.html')
