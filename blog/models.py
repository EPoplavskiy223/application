from django.db import models


class BlogPost(models.Model):
    title = models.CharField(
        max_length=20, verbose_name="Название блога", help_text="Введите название блога"
    )
    content_blog = models.TextField(
        blank=True, null=True, verbose_name="Содержимое", help_text="введите содержимое"
    )
    photo = models.ImageField(
        upload_to="photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение для блога",
    )
    date_publication = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата публикации",
        help_text="Дата публикации",
    )
    bool_blog = models.BooleanField(default=False, verbose_name="Статус публикации")
    view_cointer = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return self.title
