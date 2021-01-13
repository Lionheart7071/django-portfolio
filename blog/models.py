from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    descp = models.TextField()
    date = models.DateField()

def _str_(self):
    return self.title
