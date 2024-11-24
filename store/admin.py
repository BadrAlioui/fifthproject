from django.contrib import admin
from .models import Category, Product
# Register your models here.

#https://www.udemy.com/course/python-django-build-an-e-commerce-store-2022/learn/lecture/34534700?start=180#overview
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}