from django.contrib import admin
from .models import Blog, Category


class BlogAdmin(
    admin.ModelAdmin):  # admin yetkilerine sahip özel gösterimler için yazdık. Yani admin sayfasını blogların kontrolünde özelleştirmek yazdık.
    list_display = ("title", "is_active", "is_home", "slug")  # listede gösterilirken bu attributelar gösterilsin dedik.
    list_editable = ("is_active", "is_home")
    search_fields = ("title", "description")  # admin panele arama kısmı ekledik.
    readonly_fields = ("slug",)  # slug alanını sadece okunabilir yaptık.
    list_filter = ("category", "is_active")  # filtreleme kısmı ekledik.


admin.site.register(Blog, BlogAdmin)  # admin sayfasına dahil ediyoruz.
admin.site.register(Category)
