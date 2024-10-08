from django.core.management.base import BaseCommand
from users.models import CustomUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not CustomUser.objects.get(email='admin@sky.pro'):
            user = CustomUser.objects.create(
                email='admin@sky.pro',
                first_name='Admin',
                last_name='Admin',
                is_staff=True,
                is_superuser=True
            )

            user.set_password('qwerty123')
            user.save()
