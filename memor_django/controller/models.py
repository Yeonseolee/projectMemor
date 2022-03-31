

from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class Control_words(models.Model):
   
    user_id = models.IntegerField(default=0)
    name = models.CharField(max_length=10)
    text = models.TextField()
    title = models.CharField(max_length=10)
    # start = models.CharField(max_length=10)
    # pause = models.CharField(max_length=10)
    # restart = models.CharField(max_length=10)
    # stop = models.CharField(max_length=10)
    # created = models.DateTimeField(auto_now_add=True)
    board = ArrayField(
        models.CharField(max_length=50, blank=True),
        size=10,
    )

    def __str__(self):
        return self.user_id

