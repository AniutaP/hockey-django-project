from django import forms
from .models import Team
from django.utils.translation import gettext as _


class TeamForm(forms.ModelForm):
    name = forms.CharField(max_length=150, label=_("Name"))

    class Meta:
        model = Team
        fields = ('name', )
