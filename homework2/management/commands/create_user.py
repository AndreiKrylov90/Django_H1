from django.core.management.base import BaseCommand

from homework2.models import User2


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        #user = User2(name='John', email='john@example.com', phone='+79500000000', address='Leningrad')
        user = User2(name='James', email='james@example.com', phone='+79500050000', address='Moscow')
        user.save()
        self.stdout.write(f'{user}')