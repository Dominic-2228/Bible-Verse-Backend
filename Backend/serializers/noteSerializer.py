from rest_framework import serializers
from Backend.models import Note
from .userSerializer import UserSerializer

class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Note
        fields = [
            "id",
            "user",
            "bookId",
            "chapterId",
            "verseId",
            "title",
            "body",
        ]