from django.shortcuts import render, get_object_or_404

from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.contrib.auth import authenticate
from api_v0.serializers import *
from api_v0.models import *
from api_v0.forms import *
# from rest_framework.decorators import detail_route, list_route
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

class Userrs(viewsets.ViewSet):
    def get_permissions(self):
        # получение прав
        permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def get_users(self, request):
        user = Token.objects.get(key=token).user
        profile = Profile.objects.get(user=user)
        return (user, profile)

class User(viewsets.ViewSet):
    def get_permissions(self):
        # получение прав
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'partial_update':
            permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]

        print(self.action)
        print(permission_classes)
        return [permission() for permission in permission_classes]

    def get_auth_user_profile(self, request):
        token = self.request.headers.get('Authorization')
        token = token.replace("Token ", "")
        user = Token.objects.get(key=token).user
        profile = Profile.objects.get(user=user)
        return (user, profile)

    def create(self, request):
        # создание пользователя
        serializer = UserRegisrtSerializer(data=request.POST, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def retrieve(self, request):
        # получение профиля пользователя
        user, profile = self.get_auth_user_profile(request)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def partial_update(self, request):
        # частичное обновление профиля
        user, profile = self.get_auth_user_profile(request)
        data = request.data
        serializer = UserProfileSerializer(profile, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request):
        user, profile = self.get_auth_user_profile(request)
        user.delete()
        return Response({
            "message": f"user `{user}` has been deleted."})

class UserAuth(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def retrieve(self, request):
        login_data = request.data
        login_form = LoginForm(login_data)
        if login_form.is_valid():
            cd = login_form.cleaned_data

            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is None:
                return Response({"detail": f"Error data"})

            if user.is_active:
                token = Token.objects.get_or_create(user=user)[0]
                return Response({"detail": f"Authenticated successfully", "token": str(token)})
            else:
                return Response({"detail": f"Disabled account"})
        else:
            return Response({"detail": f"Error data"})

class UserFriendsList(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def get_auth_user_profile(self, request):
        token = self.request.headers.get('Authorization')
        token = token.replace("Token ", "")
        user = Token.objects.get(key=token).user
        profile = Profile.objects.get(user=user)
        return (user, profile)

    def retrieve(self, request):
        # получение список друзей
        user, profile = self.get_auth_user_profile(request)
        serializer = FriendsListSerializer(profile)
        friends  = serializer.data["friends"]
        return Response(friends)

    def create(self, request):
        # создание пользователя
        pass
        # serializer = UserRegisrtSerializer(data=request.POST, partial=True)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        # return Response(serializer.data)

    def destroy(self, request):
        pass
        # user, profile = self.get_auth_user_profile(request)
        # user.delete()
        # return Response({
        #     "message": f"user `{user}` has been deleted."})



# class Users(viewsets.ViewSet):

#     def list(self, request):
#         queryset = Profile.objects.all()
#         serializer = UserProfileSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         user = Token.objects.get(key=pk).user
#         profile = Profile.objects.get(user=user)
#         serializer = UserProfileSerializer(profile)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         return Response({"update":"update"})
#
#     def partial_update(self, request, pk=None):
#         # user = Token.objects.get(key=pk).user
#         # profile = Profile.objects.get(user=user)
#         # serializer = UserProfileSerializer(profile, data=request.data, partial=True)
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         # return Response(serializer.data)
#         return Response({"partial_update":"partial_update"})


# def update(self, request, pk=None):
#     user = Token.objects.get(key=pk).user
#     profile = Profile.objects.get(user=user)
#     serializer = UserProfileSerializer(data=request.data)
#
#     if serializer.is_valid():
#
#         profile.save()
#
#         user.set_password(serializer.data['password'])
#         user.save()
#         return Response({'status': 'password set'})
#     else:
#         return Response(serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)
#
#     return Response(serializer.data)
#


# class UserProfileView(generics.ListAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UserProfileSerializer
#     model = serializer_class.Meta.model
#
#     def get_queryset(self):
#         token = self.request.headers.get('Authorization')
#         token = token.replace("Token ", "")
#         user = Token.objects.get(key=token).user
#         queryset = Profile.objects.filter(user=user)
#         return queryset
#
# class UserAuthView(APIView):
#     # аунтификация пользователя
#     permission_classes = (AllowAny,)
#     def post(self, request):
#         login_data = request.data
#         login_form = LoginForm(login_data)
#         if login_form.is_valid():
#             cd = login_form.cleaned_data
#             user = authenticate(request,
#                                 username=cd['username'],
#                                 password=cd['password'])
#             if user is None:
#                 return Response({"detail": f"Error data"})
#
#             if user.is_active:
#                 token = Token.objects.get_or_create(user=user)[0]
#                 return Response({"detail": f"Authenticated successfully", "token": str(token)})
#             else:
#                 return Response({"detail": f"Disabled account"})
#         else:
#             return Response({"detail": f"Error data"})
#
# class UserCreateWiew(generics.CreateAPIView):
#     # создание пользователя
#     serializer_class = UserRegisrtSerializer
#     permission_classes = (AllowAny,)
#
# class UsersListWiew(generics.ListAPIView):
#     # список пользователей
#     serializer_class = UserListSerializer
#     permission_classes = (AllowAny,)
#     model = serializer_class.Meta.model
#
#     def get_queryset(self):
#         queryset = self.model.objects.all()
#         return queryset
#

#


#
# class UserView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request):
#         token = request.headers.get('Authorization')
#         token = token.replace("Token ", "")
#         user = Token.objects.get(key=token).user
#         pr = Profile.objects.get(user=user)
#         pr = Profile.objects.all()
#         user_perof = UserProfileListSerializer(pr, many=True)
#         return Response(user_perof.data)


# def post(self, request):
# user_form = UserRegistrationForm(request.POST)
#             if user_form.is_valid():
#                 new_user = user_form.save(commit=False)
#                 new_user.set_password(
#                     user_form.cleaned_data['password'])
#                 new_user.is_active = False
#                 new_user.save()
#                 Profile.objects.create(user=new_user)
#
#                 set_email_action(new_user)
#
#                 return HttpResponse("Вышло")
#             else:
#                 return HttpResponse("Не вышло")
#
#
#
#
#         article = request.data.get('article')
#         serializer = ArticleSerializer(data=article)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#             return Response({"success": f"Article '{article_saved.title}' created successfully"})


# from .models import Article
# from .serializers import ArticleSerializer
#
#
# class ArticleView(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response({"articles": serializer.data})
#
# #
#     def post(self, request):
#         article = request.data.get('article')
#         serializer = ArticleSerializer(data=article)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#             return Response({"success": f"Article '{article_saved.title}' created successfully"})
# #
#     def put(self, request, pk):
#         articles = Article.objects.all()
#         saved_article = get_object_or_404(articles, pk=pk)
#         data = request.data.get('article')
#         serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#             return Response({"success": f"Article '{article_saved.title}' updated successfully"})
#
#     def delete(self, request, pk):
#         articles = Article.objects.all()
#         article = get_object_or_404(articles, pk=pk)
#         article.delete()
#         return Response({
#             "message": f"Article with id `{pk}` has been deleted."}, status=204)
