from django.db import models
from datetime import date
# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title