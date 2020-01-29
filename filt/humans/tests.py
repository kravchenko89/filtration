from django.test import TestCase
from django.shortcuts import reverse

from humans.models import *


class TestUrls(TestCase):
    def test_urls1(self):
        response = self.client.get(reverse('filt-teacher'))
        self.assertEqual(response.status_code, 200)

    def test_urls2(self):
        response = self.client.get(reverse('filt-group'))
        self.assertEqual(response.status_code, 200)

    def test_urls3(self):
        response = self.client.get(reverse('filt-group'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'groups_list.html')


class Teacher(TestCase):
    def teach_test(self):
        teacher = Teacher.generate_teacher()

