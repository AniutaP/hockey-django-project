from django import forms
from django.utils.translation import gettext as _
from .models import User, Skill


class UserForm(forms.ModelForm):

    name = forms.CharField(
        max_length=150, required=True, label=_("Full name"))

    class Meta:
        model = User
        fields = ('name', 'team', 'skill')


class UserIntoTeamForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('team', )


class UpdateUserForm(UserForm):
    def clean_username(self):
        name = self.cleaned_data.get('name')
        return name


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('name', )
