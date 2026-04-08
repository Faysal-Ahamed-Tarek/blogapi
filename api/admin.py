from django.contrib import admin
from api.models import BlogPost, Category, Tag

class BlogPostAdmin(admin.ModelAdmin) :
    prepopulated_fields = {"slug": ("title",)}

class categoryAdmin(admin.ModelAdmin) : 
    prepopulated_fields = {"slug": ("name",)}

class TagAdmin(admin.ModelAdmin) : 
    prepopulated_fields = {"slug": ("name",)}

# Register your models here.
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, categoryAdmin)
admin.site.register(Tag, TagAdmin)