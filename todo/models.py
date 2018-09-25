from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Posting(models.Model):
    message = models.CharField(max_length=140, verbose_name='やること')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('home',)
