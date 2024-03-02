from django.urls import path
from hockey_django_project.users.views import (UsersListView, UserCreateView,
                                               TeamCreateView, TeamAddUserView,
                                               TeamAddUserCreateView, TeamAddUserDeleteView
                                               )


urlpatterns = [
    path('', UsersListView.as_view(), name='users_list'),
    path('create/', UserCreateView.as_view(), name='create_user'),
    path('team/create/', TeamCreateView.as_view(), name='team_create'),
    path('play/', TeamAddUserView.as_view(), name='players_list'),
    path('play/create/', TeamAddUserCreateView.as_view(), name='team_add_user'),
    path('play/clear/', TeamAddUserDeleteView.as_view(), name='team_add_user_clear'),
]
