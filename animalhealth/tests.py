from django.test import TestCase
from .models import Article,AHEnthusiast 


class AHEnthusiastTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.james = AHEnthusiast(first_name = 'James',last_name = 'Muriuki',email ='james@moringaschool.com' )
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,AHEnthusiast))

