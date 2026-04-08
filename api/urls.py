from django.urls import path
from . import views


urlpatterns = [
	path("blogposts/", views.blogposts, name="blogposts"),
	path("blogposts/<uuid:pk>/", views.blogpost_detail, name="blogpost_detail"),
	path("categories/", views.categories, name="categories"),
	path("categories/<int:pk>/", views.category_detail, name="category_detail"),
	path("tags/", views.tags, name="tags"),
	path("tags/<int:pk>/", views.tag_detail, name="tag_detail"),
]