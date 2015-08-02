from django.contrib import admin
from . import models

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published')
    list_filter = ('published',)
    date_hierarchy = 'published'
    ordering = ('-published',)

    fields = ('title', 'author', 'content', 'published')
    raw_id_fields = ('author',)
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)


admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.UserProfile)