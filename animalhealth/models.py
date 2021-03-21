from django.db import models

# Create your models here.

class AHEnthusiast(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ['first_name']

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    AHEnthusiast = models.ForeignKey(Editor)


