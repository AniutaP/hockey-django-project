from django import forms
from .models import Skill
from django.utils.translation import gettext as _


class SkillForm(forms.ModelForm):
    name = forms.CharField(max_length=150, label=_("Name"))

    class Meta:
        model = Skill
        fields = ('name', )
