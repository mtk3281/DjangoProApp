# accounts/views.py
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bgimage'] = 'assets/img/contact-bg.jpg'
        return context

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Or wherever your login template is

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bgimage'] = 'assets/img/login.jpg'
        return context