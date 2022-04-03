from re import template
from django.shortcuts import render

from django.views.generic import TemplateView, CreateView

from .forms import SignupForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(TemplateView):
    template_name= 'common/home.html'

class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('home')
    template_name = 'common/register.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name= 'common/dashboard.html'
    login_url = reverse_lazy('home')
