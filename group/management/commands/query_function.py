from django.core.management.base import BaseCommand
from django.template.loader import render_to_string

from group.models import Child, Disorder, ChildDisorder


def all_children():
    qs = ChildDisorder.objects.select_related()
    print(qs)
    return qs

def html_all_children(qs):
    html = render_to_string("background.html",{"object":qs})
    return html



class Command(BaseCommand):
    help = "query functions"

    def handle(self, *args, **options):
        qs = all_children()
        html = html_all_children(qs)

        return html