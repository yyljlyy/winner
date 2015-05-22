import json
from django.core import serializers

__author__ = 'lee'
from django.test import TestCase
from winner.models import UserProfile


class KillerTestCase(TestCase):
    def test_create(self):
        UserProfile.objects.create(name='hello', age=11, address='beijing')
        UserProfile.objects.create(name='world', age=12, address='beijing')
        UserProfile.objects.create(name='!', age=13, address='beijing')
        UserProfile.objects.filter(name='!').update(age=12)
        u = UserProfile.objects.get(name='!')
        self.assertEqual(u.age, 12, "age error")
        j = UserProfile.objects.get_queryset()
        print serializers.serialize('json', j)
