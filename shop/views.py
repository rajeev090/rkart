from django.shortcuts import render, redirect
from django.http import HttpResponse
from math import ceil
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from .models import Product, Contact
# Create your views here.


def index(request):
    products = Product.objects.all()
    electronics = Product.objects.filter(category='electronics')
    beauty = Product.objects.filter(category='beauty')
    n = len(products)
    nslides = ceil(n/5)
    # params = {'product': products, 'cor_electro': electronics, 'range': range(
    #     nslides), 'no_of_slides': nslides}
    allProds = [[products, range(nslides), nslides],
                [electronics, range(nslides), nslides], [beauty, range(1, nslides), nslides]]
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def messages(request):
    message = Contact.objects.all()
    #allmsg = [[message]]
    params = {'msg': message}
    return render(request, 'shop/messages.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        msgtype = request.POST.get('msgtype', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, phone=phone,
                          msgtype=msgtype, message=message)
        contact.save()
    return render(request, 'shop/contact.html',)


def tracker(request):
    # return render(request, 'shop/tracker.html')
    return HttpResponse("Hello this is tracker")


def checkout(request):
    # return render(request, 'shop/checkout.html')
    return HttpResponse("Hello this is checkout")


def productview(request, myid):

    product = Product.objects.filter(product_id=myid)
    return render(request, 'shop/productview.html', {'product': product[0]})
    # return render(request, 'shop/index.html')
    # return HttpResponse("Hello this is productview")


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
