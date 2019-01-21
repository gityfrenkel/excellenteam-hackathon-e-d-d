from django.urls import path

from group.views import ChildrenListView, ChildDetail, ChildCreateView

app_name = "group"

urlpatterns = [
    # path('', ),
    # path('add/', ChildCreateView.as_view(), name="create"),
    # path('<int:pk>/', ChildDetail, name="detail"),
]
