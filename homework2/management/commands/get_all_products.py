from django.core.management.base import BaseCommand
from homework2.models import Product2


class Command(BaseCommand):
    help = "Get all products."

    def handle(self, *args, **kwargs):
        products = Product2.objects.all()
        self.stdout.write(f'{products}')