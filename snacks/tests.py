from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import SnackModel

# Create your tests here.


class SnackTests(TestCase):
    def setUp(self):
        purchaser = get_user_model().objects.create(
            username="tester", password="tester")
        SnackModel.objects.create(name="Banana", purchaser=purchaser, description="Healthy Snak")

    def test_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_not_used_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateNotUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')

                
    def test_list_page_context(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        snacks = response.context['object_list']
        self.assertEqual(len(snacks), 1)
        self.assertEqual(snacks[0].name, "Banana")
        self.assertEqual(snacks[0].description, "Healthy Snak")
        self.assertEqual(snacks[0].purchaser.username, "tester")

    def test_detail_page_status_code(self):
        url = reverse('snack_detail', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('snack_detail', args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_context(self):
        url = reverse('snack_detail', args=(1,))
        response = self.client.get(url)
        snacks = response.context['snackmodel']
        self.assertEqual(snacks.name, "Banana")
        self.assertEqual(snacks.description, "Healthy Snak")
        self.assertEqual(snacks.purchaser.username, "tester")
