from django import forms
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, FormView, ListView

from group.models import Child

#
# def some_name(request):
#     foo_instance = Child.objects.create(c_name =age = models.IntegerField()
#     hobbies = models.TextField()
#     picture)
#     return render(request, 'some_name.html.html')


class ChildrenListView(ListView):
    model = Child
    ordering = ("-c_name", "-id")
    # paginate_by = 10

# def expense_list(request):
#     return render(request, "expenses/expense_list.html", {
#         'object_list': Expense.objects.order_by('-date', '-id'),
#     })


def ChildDetail(request, pk):
    o = get_object_or_404(Child, pk=pk)

    return render(request, "expenses/expense_detail.html", {
        'object': o,
    })


class ChildCreateView(CreateView):
    model = Child
    fields = "__all__"


class MyForm(forms.Form):
    are_you_sure = forms.BooleanField()


class MyFormView(FormView):
    form_class = MyForm

    def form_valid(self, form):
        assert False, form.cleaned_data
