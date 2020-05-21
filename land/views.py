from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.shortcuts import render
from django.utils.http import urlencode

from land.models import Product
from allauth.account.views import LoginView


class ShopixLogin(LoginView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_ids = self.request.GET.getlist('product_ids', [])
        products = Product.objects.filter(id__in=product_ids)
        context['products'] = products

        return context


def buy(request):
    prod_ids = request.GET.getlist('product_select', [])

    base_url = reverse('shopix_login')
    query_string = urlencode({'product_ids': prod_ids}, doseq=True)
    url = f"{base_url}?{query_string}"

    if not request.user.is_authenticated:
        return HttpResponseRedirect(url)

    return render(request, 'land/checkout.html')


def index(request):
    products = Product.objects.all()
    return render(
        request,
        'land/index.html',
        {'products': products}
    )


login_view = ShopixLogin.as_view()

