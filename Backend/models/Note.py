from django.db import models
from django.conf import settings

class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notes")
    bookId = models.CharField(max_length=10)
    chapterId = models.PositiveIntegerField()
    verseId = models.PositiveIntegerField()
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title or 'Note'} ({self.bookId} {self.chapterId}:{self.verseId})"