from django.db.models import F
from django.views.generic import ListView, DetailView

from .models import Post, Tag


class Posts(ListView):
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 4


class HomePage(Posts, ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Classic Blog Design"
        return context


class PostsByCategory(Posts, ListView):
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.kwargs["slug"]
        return context


class PostsByTag(Posts, ListView):
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Tag.objects.get(slug=self.kwargs['slug'])
        print(context["title"])
        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        self.object.views = F("views") + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class Search(ListView):
    template_name = "blog/search.html"
    context_object_name = "posts"
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get("search"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = f"search={self.request.GET.get('search')}&"
        return context
