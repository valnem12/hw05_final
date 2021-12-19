from django.contrib import admin
from django.conf import settings

from .models import Post, Group, Comment, Follow


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = settings.EMPTY_VALUE_DISPLAY


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
    search_fields = ('title',)
    empty_value_display = settings.EMPTY_VALUE_DISPLAY


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'post', 'created')
    list_filter = ('created',)
    search_fields = ('author', 'text')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('author', 'user')
    list_filter = ('author',)
    search_fields = ('author', 'user')


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
