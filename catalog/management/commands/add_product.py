import datetime
from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add products to database"

    def handle(self, *args, **kwargs):

        category, _ = Category.objects.get_or_create(name='Смартфоны')
        products = [
            {
                "name": "Xiaomi",
                "description": "Китайский телефон",
                "purchase_price": 10000,
                "created_at": datetime.datetime.now(),
                "updated_at": datetime.datetime.now(),
                "category": category,
            },
            {
                "name": "Honor",
                "description": "Китайский телефон",
                "purchase_price": 102000,
                "created_at": datetime.datetime.now(),
                "updated_at": datetime.datetime.now(),
                "category": category,
            },
            {
                "name": "Huawei",
                "description": "Китайский телефон",
                "purchase_price": 10100,
                "created_at": datetime.datetime.now(),
                "updated_at": datetime.datetime.now(),
                "category": category,
            },
            {
                "name": "Fiat",
                "description": "Китайский телефон",
                "purchase_price": 10321000,
                "created_at": datetime.datetime.now(),
                "updated_at": datetime.datetime.now(),
                "category": category,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS('Successfully added product: '
                                                     f'{product.name}'))
            else:
                self.stdout.write(self.style.WARNING('Product already exists: '
                                                     f'{product.name}'))