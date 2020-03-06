"""RestFramework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

from .views_v2 import *

app_name = "articles"

# create_user =  User.as_view({
#     'post': 'create',})
#
# get_profile_user =  User.as_view({
#     'get': 'retrieve',})
#
# update_profile_user =  User.as_view({
#     'patch': 'partial_update',})
#
# delete_user =  User.as_view({
#     'delete': 'destroy',})


user = User.as_view({
    'delete': 'destroy',
    'patch': 'partial_update',
    'get': 'retrieve',
    'post': 'create',
})

user_auth = UserAuth.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
    'post': 'create',
})

friends_list = UserFriendsList.as_view({
    'get': 'get_users',
})


urlpatterns = format_suffix_patterns([
    # path('', api_root),
    # path('snippets/', snippet_list, name='snippet-list'),

    path('user/', user, name='user'),
    path('friends_list/', friends_list, name='friends-list'),
    path('auth/', user_auth, name='user-auth'),
    path('users/',   )
    # path('profile_user', get_profile_user, name='user-profile'),
    # path('update_user', update_profile_user, name='user-profile-update'),
    # path('delete_user', delete_user, name='user-delete'),

    # path('user/<str:pk>', users_deteil, name='user-update'),
    # path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    # path('users/', user_list, name='user-list'),
    # path('users/<int:pk>/', user_detail, name='user-detail')
])

# router = DefaultRouter()
# router.register(r'users', Users, basename='users')
# urlpatterns = router.urls
#
# app_name will help us do a reverse look-up latter.
# urlpatterns = [
#     path('auth', UserAuthView.as_view()),
#     path('user_profile', UserProfileView.as_view()),
#     path('list_users',UsersListWiew.as_view()),
#     path('create_user', UserCreateWiew.as_view()),
#
#     # path('articles/<int:pk>', ArticleView.as_view())
# ]
