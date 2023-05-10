from django.db import models
import string
import random

class URL(models.Model):
    original_url = models.CharField(max_length=1024)
    short_url = models.CharField(max_length=1000, unique=True)
    visits = models.IntegerField(default=0)
    createdTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_shorturl()
        super().save(*args, **kwargs)

    def generate_shorturl(self):
        chars = string.digits + string.ascii_letters
        short_url = ''.join(random.choices(chars, k=20))
        link = URL.objects.filter(short_url=short_url).first()

        if link:
            self.generate_shorturl()

        return short_url
