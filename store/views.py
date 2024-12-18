from django.shortcuts import render, redirect, get_object_or_404
from . models import Category, Product
from .forms import ProductForm

# Create your views here.
def store(request):
    products = Product.objects.all()

    return render(request, 'store/store.html', {'products':products})

def product(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        return render(request, '404.html')
    return render(request, 'store/product.html', {'product':product})

def createProduct(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('store')
    context = {'form': form}
    return render(request, "store/store-form.html", context)

def updateProduct(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        return render(request, '404.html') 
    form = ProductForm(instance = product)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance = product)
        if form.is_valid():
            form.save()
            return redirect('store')
    context = {'form': form}
    return render(request, "store/store-form.html", context)

def deleteProduct(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        return render(request, '404.html') 
    if request.method == "POST":
        product.delete() 
        return redirect('store')
    context = {'object': product}
    return render(request, "store/delete-product.html", context)