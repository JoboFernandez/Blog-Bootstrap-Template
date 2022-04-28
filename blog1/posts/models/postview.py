from django.contrib.auth import get_user_model
from django.db import models

from . import Post

User = get_user_model()


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="views", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username