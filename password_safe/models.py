from django.db import models
from django.urls import reverse
from django.conf import settings
from django.template.defaultfilters import slugify


class Site(models.Model):
    siteName = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(null=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.siteName

    def get_absolute_url(self):
        return reverse("site_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_str = "%s %s" % (self.siteName, self.author)
            self.slug = slugify(slug_str)
        super(Site, self).save()


class Account(models.Model):
    site_name = models.ForeignKey(Site, on_delete=models.CASCADE)
    username = models.CharField(max_length=140)
    password = models.CharField(max_length=50)
    slug_field = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("home")

    def save(self, *args, **kwargs):
        if not self.slug_field:
            self.slug_field = slugify(self.username)
        return super().save(*args, **kwargs)
