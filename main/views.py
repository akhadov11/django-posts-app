from datetime import timedelta

from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from main.models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

    def get_ordering(self):
        order = self.request.GET.get('order', 'asc')
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
            return Post.objects.filter(published_on__gte=timezone.now() - timedelta(days=1)).order_by("published_on")


class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'body']
    success_url = reverse_lazy("posts-list")
