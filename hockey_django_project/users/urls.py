from django.urls import path
from hockey_django_project.users.views import (UsersListView, UserCreateView,
                                               UserUpdateView, UserDeleteView,
                                               UserIntoTeamUpdateView, MatchView,
                                               UserExitTeamView, UserAllExitTeamView,
                                               UserView,
                                               )


urlpatterns = [
    path('', UsersListView.as_view(), name='users_list'),
    path('<int:pk>/', UserView.as_view(), name='show_one_user'),
    path('create/', UserCreateView.as_view(), name='create_user'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update_user'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete_user'),
    path('<int:pk>/update/add', UserIntoTeamUpdateView.as_view(), name='update_into_team_user'),
    path('game/', MatchView.as_view(), name='match'),
    path('<int:pk>/exit/', UserExitTeamView.as_view(), name='exit_team'),
    path('clear/', UserAllExitTeamView.as_view(), name='clear_match')
]
