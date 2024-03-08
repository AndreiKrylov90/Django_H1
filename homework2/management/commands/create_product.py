from django.core.management.base import BaseCommand

from homework2.models import Product2


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        #product = Product2(name='Bread', description='White bread', price=35, amount=10)
        product = Product2(name='Milk', description='Milk 5%', price=50, amount=5)
        #product = Product2(name='Butter', description='Butter 82.5%', price=100, amount=2)
        product.save()
        self.stdout.write(f'{product}')