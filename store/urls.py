from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('product/', views.product, name="product"),
    path('create-product/', views.createProduct, name = "create-product"),
]