from time import sleep

import cv2

from light_detection import lightDetection

from django.core.management.base import BaseCommand
from django.template.loader import render_to_string

from group.models import Child

from django.core.management.base import BaseCommand
import requests
import random

from group.management import commands
from load_sound_detection import a


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
    html = render_to_string('result.html', {'object': qs})
    print(html)
    return html

def html_main(qs):
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
        v = []
        qss = all_children()
        htmlmain = html_main(qss)
        publish(htmlmain)

        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        count = 0
        num_after = 0

        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )
            num_before = num_after
            num_after = lightDetection(frame)
            count += 1
            v.append(a())


            try:
                if len(faces) > 2:
                    qs = children_by_crowed()
                    html = html_all_children(qs)
                    code = publish(html)
                    print(">", code)
                    # sleep(60)
                    qss = all_children()
                    htmlmain = html_main(qss)
                    publish(htmlmain)

                if num_after > num_before and count > 5:
                    qs = children_by_light()
                    html = html_all_children(qs)
                    code = publish(html)
                    print("STRONG LIGHT DETECTED!!!!", code)
                    # sleep(60)
                    qss = all_children()
                    htmlmain = html_main(qss)
                    publish(htmlmain)

                b = 0
                if count>50:
                    for i in range(count - 50, count):

                        if v[i] < 100:
                            b += 1
                    if b > 30:
                        qs = children_by_noise()
                        html = html_all_children(qs)
                        code = publish(html)
                        print("loud sound detected", code)
                        # sleep(60)
                        qss = all_children()
                        htmlmain = html_main(qss)
                        publish(htmlmain)


            except ConnectionError as e:
                print("!", e)


            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
