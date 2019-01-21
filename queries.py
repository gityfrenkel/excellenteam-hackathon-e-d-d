import group


def all_children():
    qs = group.models.objects.all()
    return qs