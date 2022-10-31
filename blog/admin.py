from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email address', 'body')
    action = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)