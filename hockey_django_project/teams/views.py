from hockey_django_project.teams.models import Team
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from hockey_django_project.teams.forms import TeamForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from hockey_django_project.mixins import AuthenticateMixin, AuthorizationMixin


class TeamsListView(AuthenticateMixin, ListView):
    template_name = 'teams/teams_list.html'
    model = Team
    context_object_name = 'teams'


class TeamCreateView(AuthenticateMixin, AuthorizationMixin, SuccessMessageMixin, CreateView):
    template_name = 'teams/create.html'
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy('teams_list')
    success_message = _('Team has been successfully registered')
    permission_required = 'teams.add_teams'
    permission_denied_message = _('You have no rights to add team')
    login_url = reverse_lazy('teams_list')


class TeamUpdateView(AuthenticateMixin, AuthorizationMixin, SuccessMessageMixin, UpdateView):
    template_name = 'teams/update.html'
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy('teams_list')
    success_message = _('Team has been successfully update')
    permission_required = 'teams.change_teams'
    permission_denied_message = _('You have no rights to change team')
    login_url = reverse_lazy('teams_list')


class TeamDeleteView(AuthenticateMixin, AuthorizationMixin, SuccessMessageMixin, DeleteView):
    template_name = 'teams/delete.html'
    model = Team
    success_url = reverse_lazy('teams_list')
    success_message = _('Team has been successfully delete')
    permission_required = 'teams.delete_teams'
    permission_denied_message = _('You have no rights to delete team')
    login_url = reverse_lazy('teams_list')
