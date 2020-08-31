from django.urls import path

from main.views import PostListView, PostCreateView, UserPostsView

urlpatterns = [
    path("", PostListView.as_view(), name="posts-list"),
    path("create/", PostCreateView.as_view(), name="post-create"),
    path("user_posts/", UserPostsView.as_view(), name="user-posts"),
]
