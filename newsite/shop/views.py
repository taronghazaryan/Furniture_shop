from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Order
from django.contrib.auth.models import User
from .forms import AddProduct, CreateOrderForm
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect, HttpResponseForbidden
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
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


"""All for Products"""


class ListProductView(ListView):
    model = Product
    template_name = 'shop/products_list.html'
    queryset = Product.objects.filter(archived=False)
    context_object_name = 'products'


# @login_required
class CreateProductView(PermissionRequiredMixin, CreateView):
    permission_required = ['shop.add_product',]
    """are a user superuser ,returned True or False"""
    # def test_func(self):
    #     return self.request.user.is_superuser
    #
    # def handle_no_permission(self):
    #     return HttpResponseForbidden()

    model = Product  # for teg form
    template_name = 'shop/add_product.html'  # for import teg input in html
    fields = 'name', 'price', 'description'
    success_url = reverse_lazy('shop:products')


class ProductDetailsView(DetailView):

    template_name = 'shop/product_detail.html'
    model = Product
    context_object_name = 'product'


class UpdateProductView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        return not self.request.user.is_superuser

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


# @permission_required('myauth.change_product', raise_exception=True)
class ArchivedProductView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser

    model = Product
    success_url = reverse_lazy('shop:products')

    def form_valid(self, form):
        success_url = self.success_url
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


"""All for Orders"""

# def orders(request):
#
#     if Order.objects.all():
#         all_orders = Order.objects.all()
#     else:
#         return HttpResponse('Orders not found')
#     context = {
#         'orders': all_orders
#     }
#
#     return render(request, 'shop/order_list.html', context=context)


# class ListOrderView(ListView, LoginRequiredMixin):
#     """.select_related('user'):
#     This is used to perform an SQL join to fetch related user objects along
#     with the orders in one query to avoid the N+1 query problem.
#      This is beneficial for performance when accessing related objects.
#         .prefetch_related('products'):
#     This is used to prefetch related products for each order.
#     It helps to minimize database queries by fetching related objects in a single query,
#      which can be advantageous when iterating over the queryset."""
#     queryset = (Order.objects
#                 .select_related('user')
#                 .prefetch_related('products'))


class DetailOrderView(LoginRequiredMixin, DetailView):
    # def test_func(self):
    #     return self.request.user.is_superuser

    queryset = (Order.objects
                .select_related('user')
                .prefetch_related('products'))


class CreateOrderView(LoginRequiredMixin, CreateView):

    model = Order
    fields = 'delivery_address', 'promo_code', 'products'
    template_name = 'shop/create_order.html'
    success_url = reverse_lazy('shop:user_orders')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user from the request
        return super().form_valid(form)

# def create_order(request):
#     if request.method == 'POST':
#         form = CreateOrderForm(request.POST)
#         user = User.objects.get(username='taronghazaryan')
#         if form.is_valid():
#             delivery_address = form.cleaned_data['delivery_address']
#             promo_code = form.cleaned_data['promo_code']
#             my_products = form.cleaned_data['products']
#             order, created = Order.objects.get_or_create(delivery_address=delivery_address,
#                                                          promo_code=promo_code,
#                                                          user=user
#                                                          )
#             for product in my_products:
#                 order.products.add(product)
#             if created:
#
#                 return redirect('shop:orders')
#
#             else:
#                 return HttpResponse("Order already exists")
#     else:
#         form = CreateOrderForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'shop/create_order.html', context=context)


class UpdateOrderView(LoginRequiredMixin, UpdateView):

    model = Order
    fields = 'delivery_address', 'promo_code', 'user'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('shop:order_detail',
                       kwargs={'pk': self.object.pk})


class DeleteOrderView(UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser

    model = Order
    success_url = reverse_lazy('shop:user_orders')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


@login_required
def user_orders(request):
    if request.user.is_superuser:
        user_orders_list = Order.objects.all()
    else:
        user_orders_list = Order.objects.filter(user=request.user)

    context = {
        'orders': user_orders_list,
    }

    return render(request, 'shop/my_orders.html', context=context)


