from django.shortcuts import render, redirect
from django.http import HttpResponse
from math import ceil
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from .models import Product
# Create your views here.


def index(request):
    products = Product.objects.all()
    electronics = Product.objects.filter(catagory='electronics')
    n = len(products)
    nslides = ceil(n/4)
    params = {'product': products, 'cor_electro': electronics, 'range': range(
        nslides), 'no_of_slides': nslides}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    # return render(request, 'shop/contact.html')
    return HttpResponse("Hello this is contact")


def tracker(request):
    # return render(request, 'shop/tracker.html')
    return HttpResponse("Hello this is tracker")


def checkout(request):
    # return render(request, 'shop/checkout.html')
    return HttpResponse("Hello this is checkout")


def productview(request):
    # return render(request, 'shop/index.html')
    return HttpResponse("Hello this is productview")


def search(request):
    # return render(request, 'shop/search.html')
    return HttpResponse("Hello this is search")


def register(request):
    # return render(request, 'shop/index.html')
    return HttpResponse("Hello this is register")


def cart(request):
    # return render(request, 'shop/index.html')
    return HttpResponse("Hello this is cart")


def wishlist(request):
    # return render(request, 'shop/index.html')
    return HttpResponse("Hello this is wishlist")


def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/shop")
        else:
            return render(request, 'shop/login.html')
    return render(request, 'shop/login.html')


def logoutuser(request):
    logout(request)
    return redirect("/shop")
