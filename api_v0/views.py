from django.shortcuts import render, get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from api_v0.serializers import *
from api_v0.forms import *


class AuthView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        # print(request.data.get('user'))
        # print(request.POST)
        #
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
                print(token)
                return Response({"detail": f"Authenticated successfully","token":str(token)})
            else:
                return Response({"detail": f"Disabled account"})

        else:
            return Response({"detail": f"Error data"})



class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        return Response({"ssers": "====+++++"})

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
