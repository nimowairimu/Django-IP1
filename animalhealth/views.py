from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Article

def about(request):
    return render(request, 'about.html')  

def past_days_article(request,past_date):
    

# Converts data from the string Url:

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(article_of_day)
    articles = Article.days_article(date)


    return render(request, 'all-articles/old-articles.html', {"date": date , "articles": articles})

def article_of_day(request):
    date = dt.date.today()
    articles = Article.todays_article()
    return render(request, 'all-articles/today-article.html', {"date": date,"articles": articles})

def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-articles/article.html", {"article":article})
