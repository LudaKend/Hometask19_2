from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            #email='663610kosmo85@mail.ru', is_active=True, first_name='admin', is_staff=True, is_superuser=True)
            email='admin@mail.ru', is_active=True, first_name='admin', is_staff=True, is_superuser=True)
        user.set_password('init_init')
        user.save()
