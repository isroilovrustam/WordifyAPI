from django.contrib import admin
from .models import Category, Tag, Blog, Comment, SubText, SubPicture


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    date_hierarchy = 'created_at'
    filter_horizontal = ('tags',)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(SubText)
admin.site.register(SubPicture)
