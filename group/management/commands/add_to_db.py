import names
from django.core.management.base import BaseCommand

from group.models import Child
import random


class Command(BaseCommand):
    help = "Add info to system"

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, n, *args, **options):
        Child.objects.all().delete()
        pictures = ["boy_picture.jpg", "child.jpg"]
        disorders_list = [['crowed', 'too many people in the room','play with soft things, tell someone to leave room','crowded.png'],
                          ['noise', 'strong noise','deep contact, put hands over ears, go out to a quit room','noise.png'],
                          ['light', 'strong light','go out to natural light, turn off bothering light','light.png'],
                          ['unknown', 'stranger get in','do short recognition','unknown.png']]

        for i in range(n):
            rnd_disorder = random.randint(0, 3)
            print(rnd_disorder)
            c = Child(
                name=names.get_full_name(),
                age=random.randint(5, 40),
                hobbies="biking and singing",
                picture=pictures[rnd_disorder % 2],
                disorder=disorders_list[rnd_disorder][0],
                symptom=disorders_list[rnd_disorder][1],
                solution=disorders_list[rnd_disorder][2],
                risk_level=random.randint(1, 5),
                icon=disorders_list[rnd_disorder][3],
            )
            c.save()