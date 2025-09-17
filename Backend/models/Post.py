from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    body = models.TextField()
    
    # Bible reference
    bibleBookId = models.CharField(max_length=10)   # e.g., "ROM"
    bibleChapterId = models.IntegerField()
    bibleVerseId = models.IntegerField()
    likes = models.PositiveIntegerField(default=0)

    # Dates
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.user}"