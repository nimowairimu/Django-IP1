from django.contrib import admin
from .models import Enthusiast,Article,Location

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('location',)

admin.site.register(Enthusiast)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Location)

