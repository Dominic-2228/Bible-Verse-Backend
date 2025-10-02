from rest_framework import viewsets
from Backend.models import Post
from Backend.serializers import PostSerializer
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404
from django.db.models import Count


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.annotate(likes_count=Count("user_likes"))
    def list(self, request): 
        try: 
            post = Post.objects.all()
            serializer = PostSerializer(post, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def retrieve(self, request, pk=None):
        try:
            single_post = Post.objects.filter(pk=pk).first()
            post = Post.objects.all()
            single_serializer = PostSerializer(single_post)
            post_list = []
            for user in post:
                if user.user_id == int(pk):
                    post_list.append(user)
            if len(post_list) > 0:
                return Response([PostSerializer(ser).data for ser in post_list], status=status.HTTP_200_OK)
            else: 
                return Response(single_serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        """POST /notes - Create a new note"""
        try:
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                post = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
