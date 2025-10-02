from rest_framework import serializers
from Backend.models import Post, User_Like
from django.contrib.auth import get_user_model
from .userSerializer import UserSerializer
from .userLikeSerializer import UserLikeSerializer

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    likes_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "title",
            "body",
            "date",
            "bibleBookId",
            "bibleChapterId",
            "bibleVerseId",
            "likes_count",
        ]