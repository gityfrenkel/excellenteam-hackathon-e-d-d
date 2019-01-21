import names
from django.core.management.base import BaseCommand

from group.models import Child
import random


class Command(BaseCommand):
    help = "Add Child to system"

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, n, *args, **options):

        Child.objects.all().delete()

        for i in range(n):
            o = Child(
                c_name=names.get_full_name(),
                age=random.randint(5, 120),
                hobbies="biking and singing",
                picture="boy_picture.jpg"
            )
            o.save()
