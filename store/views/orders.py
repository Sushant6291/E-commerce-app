from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product
from store.models.orders import Order
# from store.middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator  # import package to use middleware

class OrderView(View):

    # @method_decorator(auth_middleware)  # 1st way to declare middleware using method decorator
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'orders.html', {'orders': orders})
