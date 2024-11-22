from django.shortcuts import render, redirect
from . models import Category, Product
from .forms import ProductForm

# Create your views here.
def store(request):
    products = Product.objects.all()

    return render(request, 'store/store.html', {'products':products})

def product(request, pk):
    product = Product.objects.get(pk=id)
    return render(request, 'store/product.html', {'product':product})

def createProduct(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect('store')
    context = {'form': form}
    return render(request, "store/store-form.html", context)