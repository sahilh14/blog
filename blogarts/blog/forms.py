from django import forms
from django.contrib.auth.models import User

from . import models

class SearchForm(forms.Form):
    
    name = forms.CharField(max_length=100, label='')
    
class AddBlogForm(forms.Form):
    
    title = forms.CharField(max_length=100)
    message = forms.CharField(label = '', widget=forms.Textarea)
    email = forms.EmailField()

#    class Meta:
#        model = models.Blog
#        fields = ('title', 'author', 'content', 'published')

class UserForm(forms.ModelForm):
    
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = models.UserProfile
        fields = ('profile_picture',)