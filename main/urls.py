from django.urls import path

from main.views import PostListView, PostCreateView, UserPostsView

urlpatterns = [
    path("posts/", PostListView.as_view(), name="posts-list"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path("posts/user_posts/", UserPostsView.as_view(), name="user-posts")
]
