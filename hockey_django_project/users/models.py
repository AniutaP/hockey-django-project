from django.db import models
from hockey_django_project.teams.models import Team


class User(models.Model):
    name = models.CharField(max_length=150)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
