from django.contrib import admin
from group.models import Child, Disorder, Solution, ChildDisorder

admin.site.register(Child)
admin.site.register(Disorder)
admin.site.register(Solution)
admin.site.register(ChildDisorder)
