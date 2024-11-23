# Create your models here.
from django.db import models


# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
