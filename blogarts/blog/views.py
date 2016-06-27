import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from . import forms, models
from .forms import UserForm, UserProfileForm

def blog_home(request, url_name, get, post):
    
    if request.method == 'GET':
        return get(request, url_name)

    if request.method == 'POST':
        return post(request)
    raise Http404
  

def get_blog_home(request, url_name):

#    print request.META
    print "hello"
    http_referer = request.META['HTTP_REFERER']

    if url_name in http_referer and request.GET == {}:
        form = forms.AddBlogForm(initial={'message':'Write here'})
        return render(request, 'blog/blog_add_template.html', {'form':form})

    elif 'name' in request.GET:
        form = forms.AddBlogForm()
        blog = models.Blog.objects.filter(title=request.GET['name'])        
        return render(request, 'blog/blog_search_template.html', {'query':request.GET['name'],'blog':blog, 'form':form})

    form = forms.SearchForm(initial={'name':'Blog'})
    return render(request, 'blog/blog_home_template.html', {'form':form})

def post_blog_home(request):

    form = forms.AddBlogForm(request.POST)

    if form.is_valid():

        cd = form.cleaned_data
        title = cd['title']
        message = cd['message']

        b = models.Blog(title=title, author=models.Author.objects.get(name='Sahil'), content=message, published=datetime.datetime.now())
        b.save()

        return HttpResponseRedirect('/blogs/added')

    return render(request, 'blog/blog_add_template.html', {'form':form})


def blog_added(request):
    
    return render(request, 'blog/blog_added_template.html', {})
    
def register(request):
    
    registered = False
    if request.method == 'POST':
        
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_picture' in request.FILES:
                
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
            
            return HttpResponseRedirect('thanks')
        else:
            print user_form.errors, profile_form.errors
            
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    return render(request, 
           'login/register.html', 
           {'user_form':user_form, 
            'profile_form': profile_form,
            'registered':registered}
           )

def register_thanks(request):
    
    return HttpResponse('Thank you for registering\n')