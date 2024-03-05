from hockey_django_project.users.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from hockey_django_project.users.forms import UserForm, UserIntoTeamForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect


class UsersListView(ListView):
    template_name = 'users/users_list.html'
    model = User
    context_object_name = 'users'


class MatchView(ListView):
    template_name = 'users/match.html'
    model = User
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users_list')
    success_message = _('Player has been successfully registered')


class UserUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'users/update.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users_list')
    success_message = _('Player has been successfully update')


class UserIntoTeamUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'users/update.html'
    model = User
    form_class = UserIntoTeamForm
    success_url = reverse_lazy('users_list')
    success_message = _('Player has been successfully update')


class UserDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('users_list')
    success_message = _('Player has been successfully delete')


class UserExitTeamView(SuccessMessageMixin, TemplateView):
    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('match')
    success_message = _('Player successfully exit')

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.get(id=pk)
        user.team_id = None
        user.save(force_update=True)
        return redirect('match')
