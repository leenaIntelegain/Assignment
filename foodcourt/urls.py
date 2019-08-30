"""foodcourt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from restaurant.views import *
# from restaurant.api import RestaurantDetailsView

urlpatterns = [
    url(r'^$',home,name='home'),
	url(r'^home',foodcourt,name='foodcourt'),
    url(r'admin/', admin.site.urls),
    url(r'\^foodcourt/restaurants',
    	search_restaurants,
    	name='search_restaurants'),
    # url(r'foodcourt/restaurant-details',
    # 	get_foodmenu_details,
    # 	name='RestaurantDetails'),
    # url(r'foodcourt/cart',
    #     add_to_cart,
    #     name='add_to_cart'),
    # url(r'^foodcourt/cart-details', cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', cart_add, name='cart_add'),
    # url(r'^remove/(?P<product_id>\d+)/$', cart_remove, name='cart_remove'),

    url(r'^foodcourt/place-order/(?P<cart_id>\d+)/$', place_order, name='place_order'),
    url(r'^foodcourt/order-details', order_details, name='order_details'),
    url(r'^foodcourt/signup', user_signup, name='user_signup'),
    url(r'^foodcourt/user-registration', user_registration, name='user_registration'),
    url(r'^foodcourt/login', user_login, name='user_login'),
    url(r'^foodcourt/users', user_authenticate, name='user_authenticate'), 
    url(r'^foodcourt/logout', logout, name='logout'),

]
