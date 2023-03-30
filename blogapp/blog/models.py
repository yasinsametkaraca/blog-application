from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")  # upload_to ile resimlerin kaydedileceği klasörü belirttik.
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)  # slug alanı oluşturduk. Bu alanı url de kullanacağız.
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)  # category alanı oluşturduk. Bu alanı kategorileri filtrelemek için kullanacağız.

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(
            self.title)  # title a göre url ye slug ekleyecek. Mesela title yasin samet ise url de yasin-samet olacak.
        super().save(*args, **kwargs)  # save methodunu override ettik.
