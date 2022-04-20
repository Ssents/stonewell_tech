from django.test import TestCase
from django.contrib.auth import get_user_model
from product.models import Product
from django.utils import timezone

class ProductModelTest(TestCase):
    def test_making_product_successful(self):
        '''
        Test that you can make a product sucessfully
        '''
        name = "toothpaste"
        description = "Colgate herbal toothpaste" 

        product = Product.objects.create(
            name = name,
            description = description,
        )

        self.assertEqual(name, product.name)
        self.assertEqual(description, product.description)
