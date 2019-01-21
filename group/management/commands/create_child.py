import names
from django.core.management.base import BaseCommand

from group.models import Child, Disorder, ChildDisorder
import random


class Command(BaseCommand):
    help = "Add Child to system"

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, n, *args, **options):
        Disorder.objects.all().delete()
        Child.objects.all().delete()
        ChildDisorder.objects.all().delete()

        disorders_list = [('crowed', 'too much people in the room'),
                          ('unknown', 'stranger get in'),
                          ('noise', 'too much noise'),
                          ('light', 'strong light')]
        for disi in range(4):
            d, created = Disorder.objects.get_or_create(name=disorders_list[disi][0], symptom=disorders_list[disi][1])

            for i in range(n):
                c = Child(
                    name=names.get_full_name(),
                    age=random.randint(5, 120),
                    hobbies="biking and singing",
                    picture="boy_picture.jpg"
                )
                c.save()
                d.children.create(solution="take me to travel", child=c, risk_level=random.randint(1, 5))

