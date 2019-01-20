from django.db import models
from django.urls import reverse


class Child(models.Model):
    c_name = models.CharField(max_length=200)
    age = models.IntegerField(0, 120)
    hobbies = models.TextField()
    picture = models.TextField()

    def __str__(self):
        return f"{self.c_name}{self.age}{self.hobbies}{self.picture}"

    def get_absolute_url(self):
        return reverse("group:detail", args=(self.id,))

class Solution(models.Model):
    info = models.TextField()

    def __str__(self):
        return f"{self.info}"


class Disorder(models.Model):
    d_name = models.CharField(max_length=200)
    s_id = models.ForeignKey(Solution, on_delete=models.CASCADE)
    symptom = models.TextField()

    def __str__(self):
        return f"{self.d_name}{self.s_id}{self.symptom}"


class ChildDisorder(models.Model):
    d_id = models.ForeignKey(Disorder, on_delete=models.CASCADE,primary_key=True)
    c_id = models.ForeignKey(Child, on_delete=models.CASCADE,primary_key=True)
    risk_level = models.IntegerField(1, 3)

    def __str__(self):
        return f"{self.risk_level}"

