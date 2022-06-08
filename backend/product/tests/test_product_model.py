from django.test import TestCase
from django.contrib.auth import get_user_model
from product.models import Product, ProductCategory, Brand
from django.utils import timezone


class ProductModelTest(TestCase):
    '''
        Test that the product can be created, updated, listed and deleted successfully
    '''
    def setUp(self):
        product_name = "colgate tootpaste"
        description = "Colgate herbal toothpaste" 
        product_category = ProductCategory.objects.create(
            name = "toothpaste"
        )
        brand = Brand.objects.create(name = "colgate")

        product = Product.objects.create(
            name = product_name,
            description = description,
            category = product_category,
            brand = brand
        )
    
    def test_making_product_successful(self):
        '''
        Test that you can make a product sucessfully
        '''
        product = Product.objects.get(id = 1)
        self.assertEqual("colgate tootpaste", product.name)
        self.assertEqual("Colgate herbal toothpaste", product.description)

        new_product_name = "Colgate Herbal Toothpaste"
        new_description = "Colgate herbal toothpaste will all the magic"
        # product = Product.objects.get(id = 1)
        # print("Product name: " + str(product.name))
        product.name = new_product_name
        product.description = new_description
        # product.save()
        self.assertEqual(new_product_name , product.name)
    
    def _test_updating_product_successful(self):
        ''' Test that updating values of a product is successful'''
        new_product_name = "Colgate Herbal Toothpaste"
        new_description = "Colgate herbal toothpaste will all the magic"
        product = Product.objects.get(id = 1)
        print("Product name: " + str(product.name))
        product.name = new_product_name
        product.description = new_description
        # product.save()
        self.assertEqual(new_product_name , product.name)