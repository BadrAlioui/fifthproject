from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('product/<slug:slug>/', views.product, name="product"),  
    path('create-product/', views.createProduct, name="create-product"),
    path('update-product/<slug:slug>/', views.updateProduct, name="update-product"),
    path('delete-product/<slug:slug>/', views.deleteProduct, name="delete-product"),
]
