from django.contrib import admin

# Register your models here.
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp","update"]
    list_display_links = ["title", "timestamp"]
    list_filter = ["title", "timestamp"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post
        
    

admin.site.register(Post, PostAdmin)