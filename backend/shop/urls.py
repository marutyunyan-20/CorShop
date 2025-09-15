from django.urls import path
from shop.views import products_detail_view, category_list, search_products, ProductListView


app_name = 'shop'

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path("search_products/", search_products, name="search-products"),
    path('search/<slug:slug>/', category_list, name='category-list'),
    path('<slug:slug>/', products_detail_view, name='product-detail'),
]