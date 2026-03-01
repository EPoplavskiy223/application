from django.core.exceptions import ValidationError
from django.forms import BooleanField, ModelForm

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ("owner",)

    forbidden_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name:
            name_lower = name.lower()
            for forbidden_word in self.forbidden_words:
                if forbidden_word in name_lower:
                    raise ValidationError(
                        f'Название содержит запрещенное слово: "{forbidden_word}"'
                    )
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if description:
            description_lower = description.lower()
            for forbidden_word in self.forbidden_words:
                if forbidden_word in description_lower:
                    raise ValidationError(
                        f'Название содержит запрещенное слово: "{forbidden_word}"'
                    )
        return description

    def clean_purchase_price(self):
        price = self.cleaned_data.get("purchase_price")
        if price < 0:
            raise ValidationError("Цена не может быть меньше нуля")
        else:
            return price


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("bool_publication",)
