from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.shortcuts import render
from land.models import Product


def buy(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("account_login"))

    return render(request, 'land/checkout.html')


def index(request):
    products = Product.objects.all()
    return render(
        request,
        'land/index.html',
        {'products': products}
    )
