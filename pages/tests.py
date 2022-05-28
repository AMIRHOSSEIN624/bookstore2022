from django.test import TestCase
from .models import Book
from django.contrib.auth import get_user_model
from django.urls import reverse


class TestBookView(TestCase):
    def SetUp(self):
        self.user = get_user_model().objects.create()
        self.book = Book.objects.create(
            title='book1',
            author='david',
            text='hello',

        )

    def test_list_view_url(self):
        response = self.client.get('/')
        self.assertURLEqual(response.status_code, 200)

    def test_list_view_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertURLEqual(response.status_code, 200)

    def test_book_list_page(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'book1')