from rest_framework import serializers
from Backend.models import UserLike

class UserLikeSerializer(serializers.ModelSerializer):
  class Meta: 
    model = UserLike
    fields = ["user", "post"]