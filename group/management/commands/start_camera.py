import time

from django.core.management.base import BaseCommand
import requests
from group.models import Child
import random


def publish(content):
    r = requests.post('http://localhost:8976/publish/', {
        'content': content,
    })
    r.raise_for_status()
    return r.status_code


class Command(BaseCommand):
    help = "start camera"

    def handle(self, *args, **options):

        while True:
            lucky = random.randint(1, 100)
            s = f"Your lucky number is {lucky}!"
            print(s)
            try:
                code = publish(s)
                print(">", code)
            except ConnectionError as e:
                print("!", e)

            time.sleep(random.uniform(1, 4))



