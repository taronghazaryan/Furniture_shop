from django.shortcuts import render, redirect, reverse
from .models import Product, Order
from django.contrib.auth.models import User
from .forms import AddProduct, CreateOrderForm
from django.http import HttpResponse
# Create your views here.


def shop_index(request):

    return render(request, 'shop/index.html')


def products(request):
    all_product = Product.objects.all()

    context = {
        'products': all_product,
    }
    if all_product:
        return render(request, 'shop/products_list.html', context=context)
    else:
        return HttpResponse('No products')


def orders(request):

    return render(request, 'shop/orders_list.html')


def add_product(request):
    if request.method == 'POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            # url = reverse('shop:products')
            return redirect('shop:products')
    else:
        form = AddProduct()

    context = {
        'form': form,
    }

    return render(request, 'shop/add_product.html', context=context)


def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():

            Order.objects.get_or_create(**form.cleaned_data)
            return HttpResponse("Success")

    else:
        form = CreateOrderForm()

    context = {
        'form': form,
    }

    return render(request, 'shop/create_order.html', context=context)

