from django.shortcuts import render

def article_home(request):
    return render(request, 'article/article_home_template.html', {})
