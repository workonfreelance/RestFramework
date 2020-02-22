from rest_framework import serializers
from django.conf import settings
from .models import *

class User(serializers.ModelSerializer):
    class Meta:
            model = settings.AUTH_USER_MODEL
            fields = '__all__'
            # fields = ['__All__']


# class SubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         # fields = ['__all__']

#
#
# class ArticleSerializer(serializers.ModelSerializer):
#     # title = serializers.CharField()
#     # description = serializers.CharField()
#     # body = serializers.CharField()
#     # author_id = serializers.IntegerField()
#
#     class Meta:
#         model = Article
#         fields = '__all__'
#         # fields = ['__All__']

    # def create(self, validated_data):
    #     return Article.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.body = validated_data.get('body', instance.body)
    #     instance.author_id = validated_data.get('author_id', instance.author_id)
    #     instance.save()
    #     return instance