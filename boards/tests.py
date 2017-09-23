from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase

from .views import home

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
