from rest_framework import viewsets
from Backend.models import Post
from Backend.serializers import PostSerializer
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404


# reseeded database then everything broke
# was working on my post, and it may be working
class PostView(viewsets.ModelViewSet):
    def list(self, request): 
        try: 
            post = Post.objects.all()
            serializer = PostSerializer(post, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def retrieve(self, request, pk=None):
        try:
            post = get_object_or_404(Post, pk=pk)
            serializer = PostSerializer(post)
            if post.user == pk:
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        """POST /notes - Create a new note"""
        try:
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """PUT /posts/{id} - Update a post"""
        try:
            post = get_object_or_404(Post, pk=pk)
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """DELETE /posts/{id} - Delete a post"""
        try:
            post = get_object_or_404(Post, pk=pk)
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return HttpResponseServerError(ex)
