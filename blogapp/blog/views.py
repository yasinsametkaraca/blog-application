from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog

data = {
    "blogs": [
        {
            "id": 1,
            "title": "ysk",
            "image": "1.png",
            "is_active": True,
            "is_home": True,
            "description": "good"
        },
        {
            "id": 2,
            "title": "ysk",
            "image": "1.png",
            "is_active": True,
            "is_home": False,
            "description": "good"
        },
        {
            "id": 3,
            "title": "ysk",
            "image": "1.png",
            "is_active": False,
            "is_home": True,
            "description": "good"
        },
        {
            "id": 4,
            "title": "ysk",
            "image": "1.png",
            "is_active": True,
            "is_home": True,
            "description": "good"
        },
    ]
}

# http requestlerimiz.
def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True, is_active=True)
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True)
    }
    return render(request, "blog/blogs.html", context)


def blog_details(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, "blog/blog-details.html", {
        "blog": blog
    })
