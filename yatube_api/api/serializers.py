from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import get_user_model
from posts.models import Comment, Post, Follow, Group
from rest_framework import exceptions

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.filter()
                                 )
    user = SlugRelatedField(slug_field='username',
                            queryset=User.objects.filter(),
                            default=serializers.CurrentUserDefault())

    def validate_following(self, value):
        if value == self.context['request'].user:
            raise exceptions.ValidationError
        return value

    class Meta:
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
                message="На этого автора вы уже подписаны"
            )
        ]
        model = Follow
