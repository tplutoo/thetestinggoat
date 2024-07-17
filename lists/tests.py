from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


class TestHomePage(TestCase):
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')

        assert "<title>To-Do lists</title>" in html
        assert html.startswith("<html>")
        assert html.endswith("</html>")
