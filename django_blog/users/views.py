from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth import get_user_model

from .forms import RegistrationUserForm
from .forms import LoginForm


User = get_user_model()


class RegistrationView(View):

    def post(self, request):
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            new_user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
            new_user.save()
            url = reverse('main_blog:blog')
            return HttpResponseRedirect(url)
        else:
            return render(request, 'users/registration.html', {'form': form})

    def get(self, request):
        user_form = RegistrationUserForm()
        return render(request, 'users/registration.html', {'form': user_form})


class AuthenticationView(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'


class LogoutView(LogoutView):
    next_page = reverse_lazy('main_blog:blog')
