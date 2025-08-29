from rest_framework import viewsets
from Backend.models import Post
from Backend.serializers import PostSerializer

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer