from django.db import models


class Project(models.Model):
    """
    """
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    REQUIRED_FIELDS = [
        'title', 'description',
    ]
