from django.core.management.base import BaseCommand
from homework2.models import Order2


class Command(BaseCommand):
    help = "Get all orders."

    def handle(self, *args, **kwargs):
        orders = Order2.objects.all()
        self.stdout.write(f'{orders}')