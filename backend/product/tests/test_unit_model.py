from django.test import TestCase
from product.models import MeasurementUnit, MeasurementUnitCategory, SIUnit

class MeasurementUnitCategoryTestModel(TestCase):
    '''
        The purpose is to test the creation of units so that we can list items using
        the prefered unit. This requires us to test for coversion computation.
    '''

    def setUp(self):
        
        #  SI UNIT MODEL
        si_unit = "kilograms"
        si_unit_mass = SIUnit.objects.create(
            name = si_unit,
        )
        #  CATEGORY MODEL
        category_name = "mass"
        category = MeasurementUnitCategory.objects.create(
            name = category_name,
            si_unit = si_unit_mass,
        )
        # UNITS
        unit_name_1 = "pounds"
        unit_symbol_1 = "p"

        unit_name_2 = "grams"
        unit_symbol_2 = "g"

        unit_1 = MeasurementUnit.objects.create(
            name = unit_name_1,
            unit_symbol = unit_symbol_1,
            category = category,
            si_unit_coversion = 300,
        )

        unit_2 = MeasurementUnit.objects.create(
            name = unit_name_2,
            unit_symbol = unit_symbol_2,
            category = category,
            si_unit_coversion = 200,
        )
    
    def test_creating_si_unit_successful(self):
        '''Test that creating SI unit is sucessful in the SIUnit model'''
        self.assertEqual(self.si_uni_mass.name, self.s_unit)

    def test_creating_measurement_unit_category_successful(self):
        '''Test that creating MeasurementUnitCategory instance is successful'''
        self.assertEqual(self.category.name, self.name)
    
    def test_creating_measurement_successful(self):
        '''Test that creating a measurement unit is successful'''
        self.assertEqual(self.unit_1.name, self.unit_name_1)
        self.assertEqual(self.unit_1.unit_symbol, self.unit_symbol_1)
        self.assertEqual(self.unit_1.si_unit_coversion, self.si_unit_coversion_1)
