from django.db import models
from django.conf import settings



class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()

    def __str__(self):
        return f"Comment by {self.user} on Post {self.post.id}"