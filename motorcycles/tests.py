from django.test import TestCase
from .models import Motorcycles


# Create your tests here.
class ProductTests(TestCase):
    """
    Here we will define the
    test that we will run against
    our Post models
    """

    def test_str(self):
        test_name = Motorcycles(name='A product')
        self.assertEqual(str(test_name), 'A product')
