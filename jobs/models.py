from django.db import models


# Create your models here.
class Job(models.Model):
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=1)

    def __str__(self):
        return f'url: {self.url} | title: {self.title} | description: {self.description}'
