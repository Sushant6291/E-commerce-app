from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product


class Cart(View):
    def get(self, request):
        if request.method == 'GET':
            ids = list(request.session.get('cart').keys())
            products = Product.get_product_by_id(ids)
            print(products)
            return render(request, 'cart.html', {'products': products})
