from django.urls import path

from main.views import PostListView, PostCreateView

urlpatterns = [
    path("posts/", PostListView.as_view(), name="posts-list"),
    path("posts/create/", PostCreateView.as_view()),
]
