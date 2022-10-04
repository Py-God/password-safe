from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Site


class TestHomePageView(TestCase):
    def test_home_page_at_correct_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_using_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_home_page_contains_message(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Welcome to password safe.")


class SiteTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="testuser@gmail.com", password="secretuser28392"
        )
        cls.site = Site.objects.create(
            siteName="Twitter.com",
            author=cls.user,
        )

    def test_site_model(self):
        self.assertEqual(self.site.siteName, "Twitter.com")
        self.assertEqual(self.site.author.username, "testuser")
        self.assertEqual(str(self.site), "Twitter.com")
        self.assertEqual(self.site.get_absolute_url(), "/twittercom/")
