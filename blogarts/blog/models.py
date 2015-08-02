from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    
    name = models.CharField(verbose_name='namE', max_length=100)
    email = models.EmailField(verbose_name='E-maIl')
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    
    title = models.CharField(verbose_name = 'TitLe', max_length=100)
    author = models.ForeignKey(Author,verbose_name = 'WriTTen bY')
    content = models.TextField(verbose_name = 'cONtEnt')
    published = models.DateTimeField(verbose_name='WRItten ON')

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    
    profile_picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.username