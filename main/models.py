from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    published_on = models.DateTimeField("Published on", auto_now_add=True)

    def __str__(self):
        return self.title
