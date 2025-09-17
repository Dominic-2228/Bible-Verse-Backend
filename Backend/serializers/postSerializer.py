from rest_framework import serializers
from Backend.models import Post, User_Like
from django.contrib.auth import get_user_model

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):

    
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
            "likes",
        ]