from api.models import BlogPost, Category, Tag
from rest_framework import serializers


class BlogPostSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = BlogPost
        fields = "__all__"
        kwargs = {
            "title" : {"error_messages": {"min_length": "Title must be at least 5 characters long."}}
            }


class CategorySerializer(serializers.ModelSerializer) :
    class Meta :
        model = Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Tag
        fields = "__all__"