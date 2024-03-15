from django.db import models
from django.contrib.auth.models import AbstractUser
from hockey_django_project.teams.models import Team
from hockey_django_project.skills.models import Skill
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    сontact_information = models.TextField(max_length=150, null=True, blank=True, verbose_name=_('Contact information'))
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Team'))
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, null=True, blank=True, verbose_name=_('Skill'))

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return self.get_full_name()
