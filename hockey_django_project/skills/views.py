from hockey_django_project.skills.models import Skill
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from hockey_django_project.skills.forms import SkillForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class SkillsListView(ListView):
    template_name = 'skills/skills_list.html'
    model = Skill
    context_object_name = 'skills'


class SkillCreateView(SuccessMessageMixin, CreateView):
    template_name = 'skills/create.html'
    model = Skill
    form_class = SkillForm
    success_url = reverse_lazy('skills_list')
    success_message = _('Skill has been successfully registered')


class SkillUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'skills/update.html'
    model = Skill
    form_class = SkillForm
    success_url = reverse_lazy('skills_list')
    success_message = _('Skill has been successfully update')


class SkillDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'teams/delete.html'
    model = Skill
    success_url = reverse_lazy('skills_list')
    success_message = _('Team has been successfully delete')
