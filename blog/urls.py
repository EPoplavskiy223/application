from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import (BlogPostCreateView, BlogPostDeleteView,
                        BlogPostDetailView, BlogPostListView,
                        BlogPostUpdateView)
from catalog.views import ContactListView

app_name = BlogConfig.name

urlpatterns = [
    path("contact/", ContactListView.as_view(), name="contact"),
    path("", BlogPostListView.as_view(), name="blog_list"),
    path("<int:pk>/", BlogPostDetailView.as_view(), name="blog_detail"),
    path("create/", BlogPostCreateView.as_view(), name="blog_create"),
    path("<int:pk>/update/", BlogPostUpdateView.as_view(), name="blog_update"),
    path("<int:pk>/delete/", BlogPostDeleteView.as_view(), name="blog_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
