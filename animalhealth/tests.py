from django.test import TestCase
from .models import Article,Enthusiast,Location
import datetime as dt

class EnthusiastTestClass(TestCase):
    '''
    This is a an animal health enthusiast who is passionate about research of the various deseases that afects animals specicially cattle and writes articles on the causes and the possible measures that farmers can take
    Provide information to farmers so that they can identify a disease and a possible outbreak which can then be attended to before it gets out of hand
    '''
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
    # def test_update_enthusiast(self):
    #     new_first_name = 'nick'
    #     self.james.update_enthusiast(self.james.first_name, new_first_name)self.assertEqual(changed_name, self.james.'nick')
    #     changed_name = Enthusiast.objects.filter(first_name='nick')
    #     self.assertTrue(len(changed_name) > 0)


    def test_get_by_email(self):
        self.james.save_enthusiast()
        found_enthusiast = self.james.get_by_email(self.james.email)
        enthusiast = Enthusiast.objects.filter(email=self.james.email)
        self.assertTrue(found_enthusiast, enthusiast)
    
class TestLocation(TestCase):
    '''
    This model is used to show the different Loctions that the animal health enthusiast is focusing on in the article
    '''
    
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
    
    def test_search_locations(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 1)

    
    def test_update_location(self):
        new_location = 'kericho'
        self.location.update_location(self.location.id, new_location)
        changed_location = Location.objects.filter(name='kericho')
        self.assertTrue(len(changed_location) > 0)
    
    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

class ArticleTestClass(TestCase):
    def setUp(self):
        self.james= Enthusiast(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_enthusiast()

    # create a location and saving it
        self.new_location = location(name = 'Kericho')
        self.new_location.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',enthusiast = self.james)
        self.new_article.save()

        self.new_article.location.add(self.new_location)

    def tearDown(self):
        Enthusiast.objects.all().delete()
        location.objects.all().delete()
        Article.objects.all().delete()
    
    def test_get_article_today(self):
        today_article = Article.todays_article()
        self.assertTrue(len(today_article)>0)

    def test_get_article_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_article(date)
        self.assertTrue(len(article_by_date) == 0)
    
    # def test_search_article(self):
    #     search_title = self.new_article.filter(title)
    #     self.assertTrue(self.new_article)

