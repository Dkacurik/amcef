from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from app.intro.models import Post
from app.intro.serializers.post import PostModelSerializer, PostUpdateModelSerializer
from app.intro.services.post import create_post, get_post, get_user_posts


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'partial_update':
            return PostUpdateModelSerializer
        else:
            return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = create_post(**serializer.validated_data)
        if post is not None:
            return Response(PostModelSerializer(post).data, status=status.HTTP_201_CREATED)

        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, *args, **kwargs):
        instance = get_post(kwargs['pk'])
        if instance is not None:
            return Response(PostModelSerializer(instance).data)
        return Response({'message': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_id='user_posts',
        responses={200: PostModelSerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>\w+)')
    def user_posts(self, request, *args, **kwargs):
        user_id = int(kwargs['user_id'])

        user_posts = get_user_posts(user_id)

        if user_posts is not None:
            serializer = PostModelSerializer(user_posts, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
