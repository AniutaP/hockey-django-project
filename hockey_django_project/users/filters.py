from django_filters import FilterSet, ModelChoiceFilter
from django.utils.translation import gettext_lazy as _
from hockey_django_project.teams.models import Team
from hockey_django_project.skills.models import Skill
from hockey_django_project.users.models import User


class UserSkillFilter(FilterSet):

    skill = ModelChoiceFilter(
        queryset=Skill.objects.all(),
        label=_('Skill')
    )

    class Meta:
        model = User
        fields = ['skill']
        ordering = ['name']


class UserTeamFilter(FilterSet):

    team = ModelChoiceFilter(
        queryset=Team.objects.all(),
        label=_('Team')
    )

    class Meta:
        model = User
        fields = ['team']
        ordering = ['name']
