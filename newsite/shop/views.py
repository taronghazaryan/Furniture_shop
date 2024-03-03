from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Order
from django.contrib.auth.models import User
from .forms import AddProduct, CreateOrderForm
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from datetime import datetime
# Create your views here.


def shop_index(request):

    return render(request, 'shop/index.html')

# long version for show all products
# def products(request):
#     all_product = Product.objects.all()
#
#     context = {
#         'products': all_product,
#     }
#     if all_product:
#         return render(request, 'shop/products_list.html', context=context)
#     else:
#         return HttpResponse('No products')

# long version for show products details
# class ProductDetails(View):
#
#     def get(self, request: HttpRequest, pk: int):
#         product = get_object_or_404(Product, pk=pk)
#
#         context = {
#             'product': product,
#         }
#         return render(request, 'shop/product_detail.html', context=context)

# long version for work with form
# def add_product(request):
#     if request.method == 'POST':
#         form = AddProduct(request.POST)
#         if form.is_valid():
#             Product.objects.create(**form.cleaned_data)
#             # url = reverse('shop:products')
#             return redirect('shop:products')
#     else:
#         form = AddProduct()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'shop/add_product.html', context=context)


def orders(request):

    if Order.objects.all():
        all_orders = Order.objects.all()
    else:
        return HttpResponse('Orders not found')
    context = {
        'orders': all_orders
    }

    return render(request, 'shop/orders_list.html', context=context)


"""All for Products"""


class ListProductView(ListView):
    model = Product
    template_name = 'shop/products_list.html'
    queryset = Product.objects.filter(archived=False)
    context_object_name = 'products'


class CreateProductView(CreateView):

    model = Product  # for teg form
    template_name = 'shop/add_product.html'  # for import teg input in html
    fields = 'name', 'price', 'description'
    success_url = reverse_lazy('shop:products')


class ProductDetailsView(DetailView):

    template_name = 'shop/product_detail.html'
    model = Product
    context_object_name = 'product'


class UpdateProductView(UpdateView):
    model = Product
    fields = 'name', 'price', 'description'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse(
            'shop:product_details',
            kwargs={'pk': self.object.pk}
        )

    """For update created_at time"""
    def form_valid(self, form):
        form.instance.created_at = datetime.now()
        return super().form_valid(form)


class ArchivedProductView(DeleteView):

    model = Product
    success_url = reverse_lazy('shop:products')

    def form_valid(self, form):
        success_url = self.success_url
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)



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

