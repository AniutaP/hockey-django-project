from django.db import models
from hockey_django_project.teams.models import Team
from hockey_django_project.skills.models import Skill


class User(models.Model):
    name = models.CharField(max_length=150)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
