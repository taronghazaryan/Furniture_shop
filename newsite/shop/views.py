from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Order
from django.contrib.auth.models import User
from .forms import AddProduct, CreateOrderForm
from django.http import HttpResponse, HttpRequest, Http404
from django.views import View
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

    if Order.objects.all():
        all_orders = Order.objects.all()
    else:
        return HttpResponse('Orders not found')
    context = {
        'orders': all_orders
    }

    return render(request, 'shop/orders_list.html', context=context)


class ProductDetails(View):

    def get(self, request: HttpRequest, pk: int):
        product = get_object_or_404(Product, pk=pk)

        context = {
            'product': product,
        }
        return render(request, 'shop/product_detail.html', context=context)


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
        user = User.objects.get(username='taronghazaryan')
        if form.is_valid():
            delivery_address = form.cleaned_data['delivery_address']
            promo_code = form.cleaned_data['promo_code']
            my_products = form.cleaned_data['products']
            order, created = Order.objects.get_or_create(delivery_address=delivery_address,
                                                         promo_code=promo_code,
                                                         user=user
                                                         )
            for product in my_products:
                order.products.add(product)
            if created:

                return redirect('shop:orders')

            else:
                return HttpResponse("Order already exists")
    else:
        form = CreateOrderForm()

    context = {
        'form': form,
    }

    return render(request, 'shop/create_order.html', context=context)

