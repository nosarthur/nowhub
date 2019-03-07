from django.db import models

# Create your models here.
class Post(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    url = models.URLField()

