from django.urls import path

from group.views import ChildrenListView, ChildDetail, ChildCreateView

app_name = "expenses"

urlpatterns = [
    path('', ChildrenListView.as_view(), name="list"),
    path('add/', ChildCreateView.as_view(), name="create"),
    path('<int:pk>/', ChildDetail, name="detail"),
]
