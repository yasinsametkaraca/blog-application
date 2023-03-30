from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("blogs", views.blogs, name="blogs"),
    path("category/<slug:slug>", views.category_blogs, name="category_blogs"),
    path("blogs/<slug:slug>", views.blog_details, name="blog_details"),
]