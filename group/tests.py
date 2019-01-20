from django.test import TestCase
from group.models import Child, Disorder, Solution, ChildDisorder


# class ChildTestCase(TestCase):
#     def test_simple(self):
#         self.assertEqual(Child.objects.count(), 0)
#
#         o = Child(
#             date="2018-12-13",
#             amount="11.23",
#             title="Ramen",
#             description="Delicious!!!!"
#         )
#         o.save()
#
#         self.assertEqual(Expense.objects.count(), 1)
