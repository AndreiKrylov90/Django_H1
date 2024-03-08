from django.core.management.base import BaseCommand

from homework2.models import Product2, User2, Order2
from random import randint, choice


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('user_key', type=int, help='UserID')
        parser.add_argument('product_key', type=int, help='ProductID')

    def handle(self, *args, **kwargs):
        user = User2.objects.get(pk=kwargs.get('user_key'))
        product = Product2.objects.get(pk=kwargs.get('product_key'))
        total_price = product.price * randint(1, 5)

        order = Order2.objects.create(customer=user, total_price=total_price)
        order.products.add(product)
        order.save()
        self.stdout.write(f'Order #{order.pk} created with product: {product}')
