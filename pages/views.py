from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm

class HomeView(TemplateView):
    template_name = 'base.html'

class AboutView(TemplateView):
    template_name = 'pages/aboutus.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


