from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Products, ProductCategories, Basket
from .forms import RegisterForm, LoginForm, ProfileForm


def category_views(request, cat_id):
    categories = ProductCategories.objects.all()
    products = Products.objects.filter(category_id=cat_id)
    return render(request, 'products/index.html', {"products": products, "categories": categories})
 

def index(request):
    categories = ProductCategories.objects.all()
    products = Products.objects.all()
    return render(request, 'products/index.html', {"products": products, "categories": categories})


def show_product(request, pk):
    product = Products.objects.get(id=pk)
    return render(request, 'products/product.html', {'product': product})
 

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            print(form.errors)
    else:
        form = ProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)
    # total_sum = sum(basket.sum() for basket in baskets)
    # total_quantity = sum(basket.quantity for basket in baskets)
    # total_sum = 0
    # total_quantity = 0
    # for basket in baskets:
    #     total_sum += basket.sum()
    #     total_quantity += basket.quantity

    return render(request, 'profile.html', {'form': form, 'baskets': baskets}) # 'total_sum': total_sum, 'total_quantity': total_quantity


@login_required
def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
