from rest_framework import serializers
from Backend.models import User_Like

class UserLikeSerializer(serializers.ModelSerializer):
  class Meta: 
    model = User_Like
    fields = ["user", "post"]