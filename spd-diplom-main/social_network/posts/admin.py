from django.contrib import admin
from .models import Post, Like,Post_1

admin.site.register(Post)
#admin.site.register(Message)
admin.site.register(Like)
admin.site.register(Post_1)
#admin.site.register(Proba)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','text','image','created_at')
    list_display_links = ('id','text')
    search_fields = ('text','image')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','text')
    list_display_links = ('id','text')
    search_fields = ('id','text')


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')
    search_fields = ('id', 'user')

