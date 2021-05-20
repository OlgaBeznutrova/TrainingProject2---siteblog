from django import template
from django.core.cache import cache

from blog.models import Category, Post, Tag

register = template.Library()


@register.inclusion_tag("blog/menu_tpl.html")
def show_menu(menu_class="menu"):
    categories = cache.get("categories")
    if not categories:
        categories = Category.objects.all()
        cache.set("categories", categories, 30)
    return {"categories": categories, "menu_class": menu_class}


@register.inclusion_tag("blog/popular_posts_tpl.html")
def get_popular_posts(cnt=3):
    posts = Post.objects.order_by("-views")[:cnt]
    return {"posts": posts}


@register.inclusion_tag("blog/tags_tpl.html")
def get_tags():
    tags = Tag.objects.all()
    return {"tags": tags}
