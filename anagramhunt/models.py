from django.db import models
from django.conf import settings

class AddScore(models.Model):
    username = models.CharField(max_length=20, blank=False)
    score = models.PositiveSmallIntegerField(default='', blank=True)
    scoreM = models.PositiveSmallIntegerField(default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.username} + {self.score}'


