from blog.apps import BlogConfig
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import (
    BlogPostListView,
    BlogPostCreateView,
    BlogPostDetailView,
    BlogPostUpdateView,
    BlogPostDeleteView,
)
from catalog.views import ContactListView

app_name = BlogConfig.name

urlpatterns = [
    path("contact/", ContactListView.as_view(), name="contact"),
    path("", BlogPostListView.as_view(), name="blog_list"),
    path("blog/<int:pk>/", BlogPostDetailView.as_view(), name="blog_detail"),
    path("blog/create/", BlogPostCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/update/", BlogPostUpdateView.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete/", BlogPostDeleteView.as_view(), name="blog_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
