from rest_framework import serializers
from Backend.models import Comment
from .userSerializer import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # nested user info

    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
            "post",
            "body",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]