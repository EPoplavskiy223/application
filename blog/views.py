from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_cointer += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ("title", "content_blog", "photo", "date_publication")
    success_url = reverse_lazy("blog:blog_list")


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ("title", "content_blog", "photo", "date_publication", "bool_blog")
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog:blog_list")
