from rest_framework import serializers

from app.intro.models import Post


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostUpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body')
