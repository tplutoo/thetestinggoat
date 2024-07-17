from django.test import TestCase


class TestSmoke(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)
