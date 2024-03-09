from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('users_list')
    success_message = gettext_lazy('You are logged in')


def logout_view(request):
    logout(request)
    messages.success(request, 'You are logged out')
    return redirect('main')
