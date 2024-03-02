from django import forms
from django.utils.translation import gettext as _
from .models import User, Team, TeamAddUser


class UserForm(forms.ModelForm):

    first_name = forms.CharField(
        max_length=150, required=True, label=_("First name")
    )
    last_name = forms.CharField(
        max_length=150, required=True, label=_("Last name")
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UpdateUserForm(UserForm):
    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('name', )


class TeamAddUserForm(forms.ModelForm):
    class Meta:
        model = TeamAddUser
        fields = ('user', 'team')
