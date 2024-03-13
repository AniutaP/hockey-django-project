from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.utils.translation import gettext
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import ProtectedError


class AuthenticateMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, gettext('You are not logged in, please log in.'))
            return redirect(reverse_lazy('login'))

        return super().dispatch(request, *args, **kwargs)


class PermissionMixin(UserPassesTestMixin):
    permission_message = ''
    permission_url = ''

    def test_func(self):
        return self.request.user.is_superuser or self.get_object() == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.permission_message)
        return redirect(self.permission_url)


class DeleteProtectionMixin:
    rejection_message = ''
    rejection_url = ''

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.rejection_message)
            return redirect(self.rejection_url)


class AuthorizationMixin(PermissionRequiredMixin):
    permission_denied_message = ''
    login_url = ''

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect(self.login_url)
