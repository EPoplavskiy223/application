from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import ProductForm, ProductModeratorForm
from .models import Category, Product
from .services import clear_products_cache, get_products_from_cache


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = get_products_from_cache()

        category_id = self.request.GET.get("category")
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Category.objects.all().order_by("name")

        category_id = self.request.GET.get("category")
        if category_id:
            try:
                context["selected_category"] = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                context["selected_category"] = None

        return context


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user.is_superuser:
            return self.object
        if self.request.user == self.object.owner:
            self.object.save()
            return self.object
        raise PermissionDenied("У вас нет прав на редактирование продуктов")


class ContactListView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        clear_products_cache()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product") and user.has_perm(
            "catalog.delete_product"
        ):
            return ProductModeratorForm
        raise PermissionDenied("У вас нет прав на редактирование продуктов")

    def form_valid(self, form):
        clear_products_cache()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        clear_products_cache()
        return super().form_valid(form)
