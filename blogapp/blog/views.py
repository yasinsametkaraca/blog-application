from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category


# Create your views here.
def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True, is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)  # index.html sayfasına blog objesini gönderdik.


def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)  # blogs.html sayfasına blog objesini gönderdik.


def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog/blog-details.html", {
        "blog": blog,
        "categories": Category.objects.all()
    })  # blog-details.html sayfasına blog objesini gönderdik.


def category_blogs(request, slug):  # slug ile kategoriye göre blogları filtreledik.
    context = {
        # "blogs": Blog.objects.filter(is_active=True, category__slug=slug,),  # category__slug=slug ile category slug ile eşleşenleri getir dedik. (ontomany de böyle kullanılır.)
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),  # blog_set ile o kategoriye ait olan blogları getirdik. blog_set diyerek category tablosunda olmayan blok attribute a ulaştık. Çoka çok ilişkide olan diğer tabloya ulaşabiliyoruz.
        "categories": Category.objects.all(),
        "selected_category": slug  # selected_category ile seçilen kategorinin adını gönderdik.
    }
    return render(request, "blog/blogs.html", context)
