import time
import cv2

from django.core.management.base import BaseCommand
from django.template.loader import render_to_string

from group.models import Child

from django.core.management.base import BaseCommand
import requests
import random

from group.management import commands

def all_children():
    qs = Child.objects.all()
    return qs


def children_by_light():
    qs = Child.objects.filter(disorder='light')
    return qs


def children_by_crowed():
    qs = Child.objects.filter(disorder='crowed')
    print(qs)

    return qs


def children_by_noise():
    qs = Child.objects.filter(disorder='noise')
    print(qs)
    return qs


def children_by_unknown():
    qs = Child.objects.filter(disorder='unknown')
    return qs


def html_all_children(qs):
    html = render_to_string('background.html', {'object': qs})
    print(html)
    return html


def publish(content):
    r = requests.post('http://localhost:8888/publish/', {
        'content': content,
    })
    r.raise_for_status()
    return r.status_code


class Command(BaseCommand):
    help = "start camera"

    def handle(self, *args, **options):
        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        while True:

            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            try:
                if len(faces) > 0:
                    qs = all_children()
                    html = html_all_children(qs)
                    code = publish(html)
                    print(">", code)
            except ConnectionError as e:
                print("!", e)


            # time.sleep(random.uniform(1, 4))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()





