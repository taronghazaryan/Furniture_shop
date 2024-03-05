from shop.models import Product
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_info = input()
        data = product_info.split(',')

        for i in range(len(data)):
            if data[i].isdigit():
                data[i] = int(data[i])

        Product.objects.get_or_create(name=data[0], description=data[1], price=data[2])
        self.stdout.write(self.style.SUCCESS('product created successfully!!'))
