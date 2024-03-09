from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from hockey_django_project.users.forms import UserForm, UserIntoTeamForm, UpdateUserForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django_filters.views import FilterView
from hockey_django_project.users.filters import UserSkillFilter, UserTeamFilter
from hockey_django_project.mixins import (AuthenticateMixin, PermissionMixin,
                                          DeleteProtectionMixin)


class UsersListView(AuthenticateMixin, FilterView):
    template_name = 'users/users_list.html'
    model = get_user_model()
    filterset_class = UserSkillFilter
    context_object_name = 'users'


class MatchView(FilterView):
    template_name = 'users/match.html'
    model = get_user_model()
    filterset_class = UserTeamFilter
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        count = get_user_model().objects.filter(team_id__isnull=False).count()
        context['count'] = count
        return context


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    model = get_user_model()
    form_class = UserForm
    success_url = reverse_lazy('users_list')
    success_message = _('Player has been successfully registered')


class UserUpdateView(AuthenticateMixin, PermissionMixin, SuccessMessageMixin, UpdateView):
    template_name = 'users/update.html'
    model = get_user_model()
    form_class = UpdateUserForm
    success_url = reverse_lazy('users_list')
    success_message = _('Player has been successfully update')
    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('users_list')


class UserIntoTeamUpdateView(AuthenticateMixin, SuccessMessageMixin, UpdateView):
    template_name = 'users/update.html'
    model = get_user_model()
    form_class = UserIntoTeamForm
    success_url = reverse_lazy('users_list')
    success_message = _('Player has been successfully update')


class UserDeleteView(AuthenticateMixin,
                     PermissionMixin,
                     DeleteProtectionMixin,
                     SuccessMessageMixin,
                     DeleteView):
    template_name = 'users/delete.html'
    model = get_user_model()
    success_url = reverse_lazy('users_list')
    success_message = _('Player has been successfully delete')
    permission_message = _('You have no rights to change another user.')
    permission_url = 'users_list'
    rejection_message = _('Unable to delete user because it is in use')
    rejection_next_url = reverse_lazy('users_list')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserExitTeamView(AuthenticateMixin, SuccessMessageMixin, TemplateView):
    template_name = 'users/delete.html'
    model = get_user_model()
    success_url = reverse_lazy('match')
    success_message = _('Player successfully exit')

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = get_user_model().objects.get(id=pk)
        user.team_id = None
        user.save(force_update=True)
        return redirect('match')


class UserAllExitTeamView(AuthenticateMixin, SuccessMessageMixin, TemplateView):
    template_name = 'users/delete.html'
    model = get_user_model()
    success_url = reverse_lazy('match')
    success_message = _('Player successfully exit')

    def post(self, request, *args, **kwargs):
        users = get_user_model().objects.all()
        for user in users:
            if user.team_id:
                user.team_id = None
                user.save(force_update=True)
        return redirect('match')
