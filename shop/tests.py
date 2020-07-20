from django.test import TestCase
from .models import Product, Contact


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
    print(products)
    return render(request, 'shop/index.html', params)


def messages(request):
    message = Contact.objects.all()
    allmsg = [[message]]
    params = {'allmsg': allmsg}
    return render(request, 'shop/messages.html', params)
