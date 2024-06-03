from django.shortcuts import render, redirect
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id','name', 'description', 'price', 'stock', 'image']

def index(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'pages/index.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'pages/product_list.html', {'products': products})
