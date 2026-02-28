from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Название", help_text="Введите название категории"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание категории",
        help_text="Введите описание категории",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
    )
    photo = models.ImageField(
        upload_to="photo",
        blank=True,
        null=True,
        verbose_name="Фото продукта",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name="products"
    )
    purchase_price = models.IntegerField(
        verbose_name="Цена за покупку продукта",
        help_text="Укажите цену за покупку продукта",
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания продукта",
        help_text="Укажите дату создания продукта",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата изменения продукта",
        help_text="Укажите дату изменения продукта",
    )
    bool_publication = models.BooleanField(
        default=False, verbose_name="Статус публикации"
    )

    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        help_text="Укажите владельца продукта",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["created_at", "updated_at", "name", "category", "purchase_price"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]

    def __str__(self):
        return self.name
