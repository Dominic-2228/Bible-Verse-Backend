from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.http import HttpResponseServerError
from rest_framework import status
from Backend.models import UserLike
from Backend.serializers import UserLikeSerializer
from django.shortcuts import get_object_or_404

class UserLikeView(ViewSet):
    def list(self, request):
        """GET /userlikes - List all likes"""
        try:
            likes = UserLike.objects.all()
            serializer = UserLikeSerializer(likes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def retrieve(self, request, pk=None):
        """GET /userlikes/{id} - Retrieve a single like"""
        try:
            like = UserLike.objects.filter(user_id=pk)
            serializer = UserLikeSerializer(like, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        """POST /userlikes - Create a new like"""
        try:
            serializer = UserLikeSerializer(data=request.data)
            if serializer.is_valid(): 
                instance = serializer.save()
                return Response(UserLikeSerializer(instance).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """PUT /userlikes/{id} - Update a like (rarely used)"""
        try:
            like = get_object_or_404(UserLike, pk=pk)
            serializer = UserLikeSerializer(like, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """DELETE /userlikes/{id} - Delete a like"""
        try:
            like = get_object_or_404(UserLike, post_id=pk)
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return HttpResponseServerError(ex)