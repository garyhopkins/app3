from django.contrib import admin
from django.urls import path
from .views import (
    BlogDetailView,
    BlogList,
    BlogListView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    DateTime,
    PostList,
    PostListDetail,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("list", BlogList.as_view(), name="list"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("datetime/", DateTime.as_view(), name="date_time"),
    path("post-list/", PostList.as_view(), name="post-list"),
    path("post-list/<int:pk>/", PostListDetail.as_view(), name="post-list-detail"),
]
