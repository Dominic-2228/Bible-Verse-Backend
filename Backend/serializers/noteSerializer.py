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
            "book_id",
            "chapter_id",
            "verse_id",
            "title",
            "body",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]