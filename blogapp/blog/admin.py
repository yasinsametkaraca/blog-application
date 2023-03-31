from django.contrib import admin
from .models import Blog, Category


class BlogAdmin(
    admin.ModelAdmin):  # admin yetkilerine sahip özel gösterimler için yazdık. Yani admin sayfasını blogların kontrolünde özelleştirmek yazdık.
    list_display = ("title", "is_active", "is_home", "slug", "selected_categories",)  # listede gösterilirken bu attributelar gösterilsin dedik.
    list_editable = ("is_active", "is_home")
    search_fields = ("title", "description")  # admin panele arama kısmı ekledik.
    readonly_fields = ("slug",)  # slug alanını sadece okunabilir yaptık.
    list_filter = ("is_active", "categories", )  # filtreleme kısmı ekledik.

    def selected_categories(self, obj):
        html = ""
        for category in obj.categories.all():
            html += f"{category.name}, "
        return html


admin.site.register(Blog, BlogAdmin)  # admin sayfasına dahil ediyoruz.
admin.site.register(Category)
