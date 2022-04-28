from django.contrib.auth import get_user_model
from django.db import models

from . import Post

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp_created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['post', '-timestamp_created']