from product.models import Variant, Product
from django.test import TestCase

class VariantTest(TestCase):

    def _setUp(self):
        variant_name = "tootpaste large"
        size = "large"
        mass = 122
        mass_unit = "g"
        length = 100
        length_unit = "mm"
        width = 12
        width_unit = "mm"
        height = 12
        height_unit = "mm"
        mass = 1
        mass_unit = "kg"

        product = Product.objects.create(
            name = "toothpaste",
            description = "Colgate herbal toohpaste",
        )

        variant = Variant.objects.create(
            product = product,
            variant_name = variant_name,
            size = size,
            mass = mass,
            mass_unit = mass_unit,
            length = length,
            length_unit = length_unit,
            width = width,
            width_unit = width_unit,
            height = height,
            height_unit = height_unit,
        )

    def _test_create_variant_sucessful(self):
        '''
            Test that creating a product variant is successful
        '''
        self.assertEqual(self.product, self.variant.product)
        self.assterEqual(self.variant_name, self.product.variant_name)
        self.assterEqual(self.size, self.product.size)
        self.assterEqual(self.mass_unit, self.product.mass_unit)
        self.assterEqual(self.width, self.product.width)
