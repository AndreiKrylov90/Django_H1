from django.core.management.base import BaseCommand
from homework2.models import User2


class Command(BaseCommand):
    help = "Get all users."

    def handle(self, *args, **kwargs):
        users = User2.objects.all()
        self.stdout.write(f'{users}')