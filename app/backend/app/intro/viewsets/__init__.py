from rest_framework import viewsets

from app.intro.models import Post
from app.intro.serializers.post import PostModelSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
