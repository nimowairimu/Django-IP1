from django.db import models

# Create your models here.

class Enthusiast(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ['first_name']

# class Article(models.Model):
#     title = models.CharField(max_length =60)
#     post = models.TextField()
#     Enthusiast = models.ForeignKey(
#         'Enthusiast',
#         on_delete= models.DO_NOTHING,
#     )
#     pub_date = models.DateTimeField(auto_now_add=True)


