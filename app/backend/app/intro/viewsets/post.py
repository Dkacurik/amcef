from rest_framework import viewsets, status
from rest_framework.response import Response

from app.intro.models import Post
from app.intro.serializers.post import PostModelSerializer
from app.intro.services.post import validate_user, create_post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = create_post(**serializer.validated_data)
        if post is not None:
            return Response(PostModelSerializer(post).data, status=status.HTTP_201_CREATED)

        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
