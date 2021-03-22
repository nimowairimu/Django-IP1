from django.test import TestCase
from .models import Article,Enthusiast,Location


class EnthusiastTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.james = Enthusiast(first_name = 'James',last_name = 'Muriuki',email ='james@moringaschool.com' )
    
    def test_save_method(self):
        self.james.save_enthusiast()
        enthusiast = Enthusiast.objects.all()
        self.assertTrue(len(enthusiast) > 0)
    
    def test_delete_enthusiast(self):
        self.james.save_enthusiast()
        self.james.delete_enthusiast()
        enthusiast = Enthusiast.objects.all()
        self.assertTrue(len(enthusiast) == 0)

