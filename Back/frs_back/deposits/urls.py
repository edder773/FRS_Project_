from django.urls import path
from . import views

app_name = 'deposit'

urlpatterns = [
    path('products/', views.products, name = 'products'),
    path('products-option/', views.products_option, name = 'products_option'),
    path('savings/', views.savings, name = 'savings'),
    path('savings-option/', views.savings_option, name = 'savings_option'),
]
