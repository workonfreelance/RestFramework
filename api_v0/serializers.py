from rest_framework import serializers
from django.contrib.auth.models import User
from django.conf import settings
from .models import *

class UserRegisrtSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        user = User(
            email=email,
            username=username
        )
        user.set_password(validated_data['password'])
        user.save()
        profile = Profile(user=user)

        r_link = random.randint(123456789111, 999999999999)
        r_link = str(r_link)
        profile.link = r_link
        profile.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class Friends(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['surname','name','patronymic','link']

class NoFriends(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['surname','name','patronymic','link']

class FriendsListSerializer(serializers.ModelSerializer):
    friends = Friends(many=True, read_only=True)
    # black_sheet = NoFriends(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['friends']

class NoFriendsListSerializer(serializers.ModelSerializer):
    # friends = Friends(many=True, read_only=True)
    black_sheet = NoFriends(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['black_sheet']
#
#
# class UserListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')


# class User(serializers.ModelSerializer):
#     class Meta:
#             model = settings.AUTH_USER_MODEL
#             fields = '__all__'
#             # fields = ['__All__']
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username','email','password')






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