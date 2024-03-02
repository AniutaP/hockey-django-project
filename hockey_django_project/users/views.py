from hockey_django_project.users.models import User, TeamAddUser, Team
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from hockey_django_project.users.forms import UserForm, TeamForm, TeamAddUserForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


class UsersListView(ListView):
    template_name = 'users/users_list.html'
    model = User
    context_object_name = 'users'


class UserCreateView(CreateView, SuccessMessageMixin):
    template_name = 'users/create.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users_list')
    success_message = _('Player has been successfully registered')


class TeamCreateView(CreateView, SuccessMessageMixin):
    template_name = 'users/team_create.html'
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy('players_list')
    success_message = _('Team has been successfully registered')


class TeamAddUserView(ListView):
    template_name = 'users/players_list.html'
    model = TeamAddUser
    context_object_name = 'teams'


class TeamAddUserCreateView(CreateView):
    template_name = 'users/team_add_user.html'
    model = TeamAddUser
    form_class = TeamAddUserForm
    success_url = reverse_lazy('users_list')


class TeamAddUserDeleteView(TemplateView):
    template_name = 'users/clear_teams_from_players.html'
    model = TeamAddUser
    success_url = reverse_lazy('players_list')
    success_message = _('Successfully clear')

    def post(self, request, *args, **kwargs):
        TeamAddUser.objects.all().delete()
        return redirect('players_list')
