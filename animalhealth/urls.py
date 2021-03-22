from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.article_of_day,name='articleToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_article,name = 'pastArticle'),
    url(r'^article/(\d+)',views.article,name ='article') 
]

