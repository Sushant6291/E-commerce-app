from django.urls import path
from .views.login import Login, logout
from .views.signup import Signup
from .views.home import Index
from .views.cart import Cart
from .views.checkout import Checkout
from .views.orders import OrderView
from .middlewares.auth import auth_middleware  # 2nd import for middleware

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('checkout', Checkout.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),   # 2nd Way to use middleware
]