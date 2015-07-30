from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms

def blog_home(request, url_name):
    
    if request.method == 'GET':
#        print request.META
        http_referer = request.META['HTTP_REFERER']

        if url_name in http_referer and request.GET == {}:
            return render(request, 'blog/blog_home_template.html', {'form':None})

        elif 'name' in request.GET:
            return render(request, 'blog/blog_search_template.html', {'query':request.GET['name']})
            
    if request.method == 'POST':
        return HttpResponseRedirect('/blogs/added')
        
    form = forms.SearchForm(initial={'name':'Blog'})
    return render(request, 'blog/blog_home_template.html', {'form':form})

def blog_added(request):
    return render(request, 'blog/blog_added_template.html', {})