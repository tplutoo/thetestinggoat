import pytest
from django.test import TestCase
from pytest_django.asserts import assertContains, assertTemplateUsed


class TestHomePage(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "lists/home.html")

