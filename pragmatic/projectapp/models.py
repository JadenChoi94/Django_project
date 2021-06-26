from django.db import models


class Project(models.Model):
    image = models.ImageField(upload_to='profile/', null=True)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now=True)
