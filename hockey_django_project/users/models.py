from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    status = models.ForeignKey('Status', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.first_name


class Team(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class TeamAddUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    team = models.ForeignKey(Team, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = _('TeamAddUser')


class Status(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
