from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    # article = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all())
    class Meta:
        model = Comment
        fields = '__all__'
        # exclude = ('user','article',)
        # read_only_fields = ('article',)
    # def create(self, validated_data):
    #     validated_data['user'] = self.context['request'].user
        # return super().create(validated_data)

class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        # fields = ('title', 'content')
        # exclude = ('user',)
        fields = '__all__'


    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = rep.pop('comment_set', [])
        return rep
