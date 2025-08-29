from django.db import models
from django.conf import settings

class UserLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="user_likes")

    class Meta:
        unique_together = ("user", "post")  # ensures a user can only like a post once

    def __str__(self):
        return f"{self.user} liked {self.post}"