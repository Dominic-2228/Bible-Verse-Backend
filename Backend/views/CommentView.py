from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.http import HttpResponseServerError
from rest_framework import status
from Backend.models import Comment
from Backend.serializers import CommentSerializer
from django.shortcuts import get_object_or_404

class CommentView(ViewSet):
    def list(self, request):
        """GET /comments - List all comments"""
        try:
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def retrieve(self, request, pk=None):
        """GET /comments/{id} - Retrieve a single comment"""
        try:
            comment = get_object_or_404(Comment, pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        """POST /comments - Create a new comment"""
        try:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """PUT /comments/{id} - Update a comment"""
        try:
            comment = get_object_or_404(Comment, pk=pk)
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """DELETE /comments/{id} - Delete a comment"""
        try:
            comment = get_object_or_404(Comment, pk=pk)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return HttpResponseServerError(ex)