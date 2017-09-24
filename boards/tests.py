from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase

from .views import home, boards_topic
from .models import Board

# Create your tests here.


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        """We are testing the status code of the response."""
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        """The test will make sure the URL /, which is the root URL, is returning the home view."""
        view = resolve('/')
        self.assertEquals(view.func, home)


class BoardsTopicTest(TestCase):
    def setup(self):
        """The method, will created a Board instance, so to use it in the tests."""
        Board.objects.create(name='Materialize CSS', description='A beautiful way to create')

    def test_boards_topic_view_success_status_code(self):
        """Test if the View will return 200"""
        url = reverse('boards_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_boards_topic_view_not_found_status_code(self):
        """Test if the View will not return 200, instead bring 404"""
        url = reverse('boards_topic', kwargs={'pk': 799})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_boards_topic_url_resolves_to_boards_topic_view(self):
        """The test will make sure the boards_topic URL, is returning the boards_topic view."""
        view = resolve('/boards/1/')
        self.assertEquals(view.func, boards_topic)
