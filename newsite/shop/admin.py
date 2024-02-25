from django.contrib import admin
from .models import Product, Order
from django.db.models import QuerySet
from django.http import  HttpRequest
# Register your models here.




class OrderInLine(admin.TabularInline):
    model = Product.orders.through


@admin.action(description='Archive Products')
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description='Unarchive Products')
def mark_unarchived(modeladmin: admin.ModelAdmin, queryset: QuerySet):
    queryset.update(archived=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    actions = [
        mark_archived,
        mark_unarchived,
    ]

    inlines = [
        OrderInLine,
    ]

    list_display = 'pk', 'name', 'description_short', 'price', 'created_at', 'archived'
    list_display_links = 'pk', 'name'
    ordering = 'pk',
    search_fields = 'name', 'description'
    fieldsets = [
        (None, {
            'fields': ('name', 'description')
        }),
        ('Price options', {
            'fields': ('price', ),
            'classes': ('collapse', 'wide')
        }),
        ('Extra Options', {
            'fields': ('archived',),
            'classes': ('collapse',),
            'description': 'Extra options. Field "archived" is for soft delete',
        })
    ]

    def description_short(self, obj: Product):
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + '...'


class ProductInLine(admin.StackedInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInLine,
    ]

    list_display = 'pk', 'delivery_address', 'promo_code', 'user', 'created_at'


