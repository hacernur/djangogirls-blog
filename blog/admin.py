from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_date', 'published_date')
    list_filter = ('author', 'title')


admin.site.register(Post, PostAdmin)
