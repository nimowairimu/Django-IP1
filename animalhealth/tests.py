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
    
    # def test_update_enthusiast(self):
    #     self.james.save_enthusiast()
    #     Changed_enthusiast = self.james.filter(first_name).update(first_name = "Nick")
    #     self.assertEqual(changed_enthusiast.first_name, "Nick")

    def test_get_by_email(self):
        self.james.save_enthusiast()
        found_enthusiast = self.james.get_by_email(self.james.email)
        enthusiast = Enthusiast.objects.filter(email=self.james.email)
        self.assertTrue(found_enthusiast, enthusiast)
    
class TestLocation(TestCase):
    
    def setUp(self):
        self.location = Location(name = 'Samburu')
        self.location.save_location()

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0 )
    
    
    def test_get_locations(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 1)
    
    # def test_update_location(self):
    #     new_location = 'kericho'
    #     self.location.update_location(self.location.id, new_location)
    #     changed_location = Location.objects.filter(name='kericho')
        # self.assertTrue(len(changed_location) > 0)