import names
from django.core.management.base import BaseCommand

from group.models import Child
import random


class Command(BaseCommand):
    help = "Add info to system"

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, n, *args, **options):
        fill_info = {'name': ['David', 'Sarah', 'Noam', 'Shaked', 'Chaim', 'Rachel'],
                     'full_name': ['David Cohen', 'Sarah Linn', 'Noam Levi', 'Shaked Smith', 'Chaim Tiko',
                                   'Rachel Traub'],
                     'age': ['8', '6', '7', '10', '9', '6'],
                     'hobbies': ['singing', 'Singing and baking', 'Drawing and biking', 'Drawing and baking',
                                 'Singing and dancing', 'drawing'],
                     'disorder': ['Loud noise', 'Strong light', 'Crowded space', 'Crowded space', 'Strong light',
                                  'Loud noise'],
                     'How to cope': ['play with soft things, or put his hands over his ears.',
                                     'play with soft things, or put her hands over her eyes.',
                                     'draw a picture or get intense physical contact.',
                                     'draw a picture or get some natural light through the window.',
                                     'draw a picture or get some natural light through the window.',
                                     'draw a picture or put hands over ears.'],
                     'Risk level': ['1', '1', '1', '2', '2', '2'],
                     'picture': ['david.jpg', 'sara.jpg', 'noam.jpg', 'shaked.jpg', 'chaim.jpg', 'rachel.jpg'],
                     'icon': ['noise.png', 'light.png', 'crowded.png', 'crowded.png', 'light.png', 'noise.png']}
        Child.objects.all().delete()

        for i in range(6):
            c = Child(
                name=fill_info['name'][i],
                full_name=fill_info['full_name'][i],
                age=fill_info['age'][i],
                hobbies=fill_info['hobbies'][i],
                picture=fill_info['picture'][i],
                disorder=fill_info['disorder'][i],
                solution=fill_info['How to cope'][i],
                risk_level=fill_info['Risk level'][i],
                icon=fill_info['icon'][i],
            )
            c.save()