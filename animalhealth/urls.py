from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns=[
    url(r'^$',views.article_of_day,name='articleToday'),
    url(r'^$',views.about , name = 'about'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_article,name = 'pastArticle'),
    url(r'^article/(\d+)',views.article,name ='article'),
    # url(r'admin/', admin.site.urls, name='admin' ),
    url(r'',(views.article_of_day), name='articleOfDay') 

    
]

