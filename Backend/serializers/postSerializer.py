from rest_framework import serializers
from Backend.models import Post, User_Like
from django.contrib.auth import get_user_model

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    # Optional: include the user's likes
    liked_by_users = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
        source='likes'  # this uses the related_name="likes" on UserLike
    )
    
    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "title",
            "body",
            "bibleBookId",
            "bibleChapterId",
            "bibleVerseId",
            "feelingId",
            "likes",
            "liked_by_users",
        ]