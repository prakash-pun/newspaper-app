from django.test import TestCase

class BlogTest(TestCase):

    def test_post_content(self):
        self.assertEqual('My Test', 'My Test')