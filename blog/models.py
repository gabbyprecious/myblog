from django.db import models
from django.contrib.auth import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
    comment = models.TextField()
    post = models.ForeignKey("Post", related_name="post_comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
