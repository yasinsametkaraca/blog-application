from django.http.response import HttpResponse
from django.shortcuts import render

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
        "blogs": data["blogs"]
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, "blog/blogs.html", context)


def blog_details(request, id):
    blogs = data["blogs"]
    selectedBlog = None

    for blog in blogs:
        if blog["id"] == id:
            selectedBlog = blog

    return render(request, "blog/blog-details.html", {
        "blog": selectedBlog
    })
