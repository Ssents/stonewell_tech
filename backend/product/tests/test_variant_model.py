from product.models import Variant, Product
from django.test import TestCase

class VariantTest(TestCase):

    def setUp(self):
        variant_name = "tootpaste large"
        size = "large"
        size_unit = "SML"
        weight = 122
        weight_unit = "g"
        length = 100
        length_unit = "mm"
        width = 12
        width_unit = "mm"
        height = 12
        height_unit = "mm"

        product = Product.objects.create(
            name = "toothpaste",
            description = "Colgate herbal toohpaste",
        )

        variant = Variant.objects.create(
            product = product,
            variant_name = variant_name,
            size = size,
            size_unit = size_unit,
            weight = weight,
            weight_unit = weight_unit,
            length = length,
            length_unit = length_unit,
            width = width,
            width_unit = width_unit,
            height = height,
            height_unit = height_unit, 
        )

    def test_create_variant_sucessful(self):
        '''
            Test that creating a product variant is successful
        '''
        self.assertEqual(self.product, self.variant.product)
        self.assterEqual(self.variant_name, self.product.variant_name)
        self.assterEqual(self.size, self.product.size)
        self.assterEqual(self.weight_unit, self.product.weight_unit)
        self.assterEqual(self.width, self.product.width)
