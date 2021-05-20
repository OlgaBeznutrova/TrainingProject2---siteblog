from django.urls import path

from .views import HomePage, PostsByCategory, PostsByTag, PostDetail, Search

urlpatterns = [
    path('', HomePage.as_view(), name="home_page"),
    path('category/<str:slug>/', PostsByCategory.as_view(), name="category"),
    path('tag/<str:slug>/', PostsByTag.as_view(), name="tag"),
    path('post/<str:slug>/', PostDetail.as_view(), name="post"),
    path('seach/', Search.as_view(), name="search"),

]
