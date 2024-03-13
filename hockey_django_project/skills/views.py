from hockey_django_project.skills.models import Skill
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from hockey_django_project.skills.forms import SkillForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from hockey_django_project.mixins import AuthenticateMixin, AuthorizationMixin


class SkillsListView(AuthenticateMixin, ListView):
    template_name = 'skills/skills_list.html'
    model = Skill
    context_object_name = 'skills'


class SkillCreateView(AuthenticateMixin, AuthorizationMixin, SuccessMessageMixin, CreateView):
    template_name = 'skills/create.html'
    model = Skill
    form_class = SkillForm
    success_url = reverse_lazy('skills_list')
    success_message = _('Skill has been successfully registered')
    permission_required = 'skills.add_skills'
    permission_denied_message = _('You have no rights to add skill')
    login_url = reverse_lazy('skills_list')


class SkillUpdateView(AuthenticateMixin, AuthorizationMixin, SuccessMessageMixin, UpdateView):
    template_name = 'skills/update.html'
    model = Skill
    form_class = SkillForm
    success_url = reverse_lazy('skills_list')
    success_message = _('Skill has been successfully update')
    permission_required = 'skills.change_skills'
    permission_denied_message = _('You have no rights to change skill')
    login_url = reverse_lazy('skills_list')


class SkillDeleteView(AuthenticateMixin, AuthorizationMixin, SuccessMessageMixin, DeleteView):
    template_name = 'teams/delete.html'
    model = Skill
    success_url = reverse_lazy('skills_list')
    success_message = _('Skill has been successfully delete')
    permission_required = 'skills.delete_skills'
    permission_denied_message = _('You have no rights to delete skill')
    login_url = reverse_lazy('skills_list')
