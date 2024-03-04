from hockey_django_project.teams.models import Team
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from hockey_django_project.teams.forms import TeamForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages


class TeamsListView(ListView):
    template_name = 'teams/teams_list.html'
    model = Team
    context_object_name = 'teams'


class TeamView(DetailView):
    template_name = 'teams/show_one_team.html'
    model = Team
    context_object_name = 'team'


class TeamCreateView(SuccessMessageMixin, CreateView):
    template_name = 'teams/create.html'
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy('teams_list')
    success_message = _('Team has been successfully registered')


class TeamUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'teams/update.html'
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy('teams_list')
    success_message = _('Team has been successfully update')


class TeamDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'teams/delete.html'
    model = Team
    success_url = reverse_lazy('teams_list')
    success_message = _('Team has been successfully delete')
