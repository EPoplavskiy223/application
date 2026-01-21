from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactListView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductCreateView(CreateView):
    model = Product
    fields = (
        "name",
        "description",
        "photo",
        "category",
        "purchase_price",
        "created_at",
    )
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = (
        "name",
        "description",
        "photo",
        "category",
        "purchase_price",
        "created_at",
        "updated_at",
    )
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
