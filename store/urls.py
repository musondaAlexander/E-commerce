from django.urls import path

from .views.home import Home 
from .views.account import Account
from .views.checkout import Checkout
from .views.wishlist import Wishlist
from .views.cart import Cart
from .views.pages import Contact
from .views.pages import Error404
from .views.pages import FAQ
from .views.pages import Privacy
from .views.login import Login
from .views.products import ProductDetailsAffliate
from .views.products import ProductDetailsGroup
from .views.products import ProductDetailsVariable
from .views.products import ProductDetailsDefault
from .views.pages import Discover
from .views.pages import About
from .views.products import Compare

urlpatterns = [
     path('', Home.as_view(), name='store-home'),
     path('account', Account.as_view(), name='store-account'),
     path('checkout', Checkout.as_view(), name='store-checkout'),
     path('wishlist', Wishlist.as_view(), name='store-wishlist'),
     path('cart', Cart.as_view(), name='store-cart'),
     path('contact', Contact.as_view(), name='store-contact'),
     path('error404', Error404.as_view(), name='store-error404'),
     path('faq', FAQ.as_view(), name='store-faq'),
     path('privacy', Privacy.as_view(), name='store-privacy'),
     path('login', Login.as_view(), name='store-login'),
    #  urls for product details
     path('product-details-affliate', ProductDetailsAffliate.as_view(), name='store-product-details-affliate'),
     path('product-details-group',ProductDetailsGroup.as_view(), name='store-product-details-group'),
     path('product-details-variable', ProductDetailsVariable.as_view(), name='store-product-details-variable'),
     path('product-details-default', ProductDetailsDefault.as_view(), name='store-product-details-default'),
     path('compare', Compare.as_view(), name='store-compare'),
     path('about', About.as_view(), name='store-about'),
    path('discover', Discover.as_view(), name='store-discover'),
    # login signup cart checkout wishlist account contact Error404 FAQ Privacy  
]
