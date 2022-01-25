from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


from posts.models import Comment, Post, Follow, Group


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
                                 read_only=True,)
    user = SlugRelatedField(slug_field='username',
                            read_only=True,)

    def validate(self, data):
        if Follow.objects.filter(
            user=self.context["request"].user, following=data["following"]
        ).exists():
            raise serializers.ValidationError(
                {"error": "Подписка уже существует"}
            )
        return data

    class Meta:
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset = Follow.objects.all(),
                fields=['user', 'following'],
                message = "На этого автора вы уже подписаны"
            )
        ]
        model = Follow
