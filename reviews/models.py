from django.db import models
from django.conf import settings

class AddReview(models.Model):
    login = models.CharField(max_length=20, blank=False)
    review = models.TextField(default='', blank=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.login} {self.review}'