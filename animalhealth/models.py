from django.db import models

# Create your models here.

class Enthusiast(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    # location = models.ForeignKey(Location)
    # article = models.ForeignKey(Article)

   
    @classmethod
    def get_by_email(cls, email):
       image = cls.objects.filter(email=email).all()
       return email
    
    @classmethod
    def update_enthusiast(cls, first_name, value):
        cls.objects.filter(first_name=first_name).update(first_name=value)

    #
    def __str__(self):
        return self.first_name
    
    def save_enthusiast(self):
        self.save()
    
    def delete_enthusiast(self):
        self.delete()
    

    
    class Meta:
        ordering = ['first_name']

class Location(models.Model):
    name = models.CharField(max_length = 40)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations
    
    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(name=value)


    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()

       

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    Enthusiast = models.ForeignKey(
        'Enthusiast',
        on_delete= models.DO_NOTHING,
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ManyToManyField(Location)

