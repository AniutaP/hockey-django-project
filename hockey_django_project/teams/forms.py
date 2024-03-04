from django import forms
from .models import Team
from django.utils.translation import gettext as _


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name', )
