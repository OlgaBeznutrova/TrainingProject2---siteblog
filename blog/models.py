from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True)  # verbose_name="Url категории",

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title", ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)  # verbose_name="Url тега",

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tag", kwargs={"slug": self.slug})


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.SlugField(max_length=50, unique=True)  # verbose_name="Url поста"
    author = models.CharField(max_length=100, verbose_name="Автор")
    content = models.TextField(blank=True)
    quote = models.CharField(max_length=255, blank=True, verbose_name="Цитата")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Опубликовано")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    views = models.IntegerField(default=0, verbose_name="Кол-во просмотров")
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name="posts", verbose_name="Категория")
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})
