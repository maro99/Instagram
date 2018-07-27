from members.serializers import UserSerializer
from .models import Post

from rest_framework import serializers

# class PostSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Post
#         fields = (
#             'pk',
#             'author',
#             'photo',
#             'content',
#             'created_at',
#             'likes',
#             'tags',
#         )


class PostBaseSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)

    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'photo',
            'content',
            'created_at',
            'likes',
            'tags',
        )

        read_only_fields = (
            'author',
        )


class PostListSerializer(PostBaseSerializer):
    pass


class PostDetailSerializer(PostBaseSerializer):
    class Meta(PostBaseSerializer.Meta):
        fields = PostBaseSerializer.Meta.fields + ('photo', 'content',)




