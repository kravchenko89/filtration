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

    def test_tech_edit(self):
        teach = {
            'first_name': 'Alex', 'last_name': 'Underwood',
            'country': 'United States of America',
            'lesson': 'History', 'birth_date': '1999-10-03',
            'email': 'rhondasmith@yahoo.com', 'phone': '5777116752',
            'address': '7862 Lee Glen Apt. 001 Benjaminview, WA 71403',
            'credit_card': '6011244588503852'
        }

        teacher = Teacher.generate_teacher()

        response = self.client.post(reverse('edit-teacher', args=[teacher.id]), teach)

        assert response.status_code == 302

        teach['first_name'] = 'WRONG'
        teach['last_name'] = 'WRONG'
        teach['country'] = 'WRONG'
        teach['lesson'] = 'WRONG'
        teach['birth_date'] = 'WRONG'
        teach['email'] = 'WRONG'
        teach['phone'] = 'WRONG'
        teach['address'] = 'WRONG'
        teach['credit_card'] = 'WRONG'
        response = self.client.post(reverse('edit-teacher', args=[teacher.id]), teach)
        assert response.status_code == 200
