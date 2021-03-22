from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt




def article_of_day(request):
    date = dt.date.today()
    return render (request,'all-articles/today-article.html',{"date": date})


    
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

    return render(request, 'all-articles/old-articles.html', {"date": date})
