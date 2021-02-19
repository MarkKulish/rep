from django.urls import path

from product.views import *

urlpatterns = [
    path('', homepage, name='index-page'),
    path('product/<slug:category_slug>/', products_list, name='products_list'),
    path('products/details/<int:product_id>/', product_details, name='product-details')
]
