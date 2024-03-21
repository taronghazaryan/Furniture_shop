from django.test import TestCase
from .views import ProductDetailsView
from .models import Product
from django.shortcuts import reverse

# Create your tests here.


class ProductDetailsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product = Product.objects.create(name='aman', price=200)

    @classmethod
    def tearDownClass(cls):
        cls.product.delete()

    def test_get_product(self):
        response = self.client.get(reverse('shop:product_details', kwargs={'pk': self.product.pk}))

        self.assertEquals(response.status_code, 200)


