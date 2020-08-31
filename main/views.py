from datetime import timedelta

from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from main.models import Post


class PostListView(generic.ListView):
    """
    List of all posts.
    """

    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"

    def get_ordering(self):
        order = self.request.GET.get("order", "asc")
        return order

    def get_last_param(self):
        last = self.request.GET.get("last", "day")
        return last

    def get_queryset(self):
        order = self.get_ordering()
        last = self.get_last_param()
        if order == "asc":
            return Post.objects.all().order_by("published_on")
        elif order == "desc":
            return Post.objects.all().order_by("-published_on")
        if last == "day":
            return Post.objects.filter(
                published_on__gte=timezone.now() - timedelta(days=1)
            ).order_by("published_on")


class PostCreateView(generic.CreateView):
    """
    Creation of a new post.
    """

    model = Post
    template_name = "post_create.html"
    fields = ["title", "body", "image"]
    success_url = reverse_lazy("posts-list")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        return super().form_valid(form)


class UserPostsView(generic.ListView):
    """
    All posts by a particular user.
    """

    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author__id=user.pk)
