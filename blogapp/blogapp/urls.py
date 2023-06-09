"""blogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path('account/', include("account.urls")),  # account uygulamasındaki urls.py dosyasını buraya dahil ettik.
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # media dosyalarını göstermek için ekledik. http://127.0.0.1:8000/images/blogs/2.jpg gibi.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # static dosyalarını göstermek için ekledik.
