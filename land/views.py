from django.shortcuts import render
from land.models import Product


def index(request):
    products = Product.objects.all()
    return render(
        request,
        'land/index.html',
        {'products': products}
    )
