from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .serializers import BlogPostSerializer, CategorySerializer, TagSerializer
from .models import BlogPost, Category, Tag


class BlogPostPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 5



@api_view(["GET", "POST"])
def blogposts(request):
    if request.method == "GET":
        data = BlogPost.objects.all().order_by("-created_at")
        paginator = BlogPostPagination()
        page = paginator.paginate_queryset(data, request)
        serializer = BlogPostSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    if request.method == "POST":
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def blogpost_detail(request, pk):
    try : 
        post = BlogPost.objects.get(pk=pk)
    except :
        return Response({"detail": "Blog post not found."}, status=404)

    if request.method == "GET":
        serializer = BlogPostSerializer(post)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BlogPostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == "PATCH":
        serializer = BlogPostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    if request.method == "DELETE":
        post.delete()
        return Response(status=204)



@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        data = Category.objects.all().order_by("name")
        serializer = CategorySerializer(data, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET", "PUT", "PATCH", "DELETE"])
def category_detail(request, pk):
    try : 
        category = Category.objects.get(pk=pk)
    except :
        return Response({"detail": "Category not found."}, status=404)

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    if request.method in ["PUT", "PATCH"]:
        partial = request.method == "PATCH"
        serializer = CategorySerializer(category, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def tags(request):
    if request.method == "GET":
        data = Tag.objects.all().order_by("name")
        serializer = TagSerializer(data, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def tag_detail(request, pk):
    try :
        tag = Tag.objects.get(pk=pk)
    except :
        return Response({"detail": "Tag not found."}, status=404)

    if request.method == "GET":
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    if request.method in ["PUT", "PATCH"]:
        partial = request.method == "PATCH"
        serializer = TagSerializer(tag, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    tag.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)