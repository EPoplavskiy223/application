from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()