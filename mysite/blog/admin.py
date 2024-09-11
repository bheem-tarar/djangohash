from django.contrib import admin
from .models import Category, Tag, Post,Comment,Contact

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title'] 

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name'] 

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'published_date')
    list_filter = ('author', 'created_at', 'category', 'tags')
    search_fields = ('title', 'content', 'author__username', 'category__title',)
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ['author', 'category', 'tags']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created_at', 'timestamp', 'status')
    list_filter = ('status', 'created_at', 'timestamp', 'post')
    search_fields = ('name', 'email', 'message')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    # raw_id_fields = ('post',)

# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'subject', 'created_at', 'status')
#     list_filter = ('status', 'created_at')
#     search_fields = ('name', 'email', 'subject', 'phone')
#     readonly_fields = ('created_at', 'timestamp', 'utimestamp')
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at')

# admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)


