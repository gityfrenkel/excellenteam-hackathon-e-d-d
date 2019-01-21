from django.contrib import admin
from group.models import Child, Disorder, ChildDisorder

admin.site.register(Child)
admin.site.register(Disorder)
admin.site.register(ChildDisorder)
