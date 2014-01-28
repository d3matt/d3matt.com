from django.contrib import admin
from blog.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'post_date', 'update_date', 'edited')

admin.site.register(BlogPost, BlogPostAdmin)
