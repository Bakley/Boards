from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase

from .views import home, boards_topic
from .models import Board

# Create your tests here.


class HomeTests(TestCase):
    """Home Views test"""

    def setup(self):
        """The method will create a Home instance, to use in the test"""
        self.board = Board.objects.create(name='Materialize CSS', description='A beautiful way to create')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        """We are testing the status code of the response."""
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        """The test will make sure the URL /, which is the root URL, is returning the home view."""
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_links_to_topics_page(self):
        """Test if The homepage has a link to take the visitor to the topics page of a given Board"""
        boards_topic_url = reverse('boards_topic', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(boards_topic_url))  # test if the response body contains a given text


class BoardsTopicTest(TestCase):
    """Boards Topic view test"""

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

    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse('boards_topic', kwargs={'pk': 1})
        response = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
