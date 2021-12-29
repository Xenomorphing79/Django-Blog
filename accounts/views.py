from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView, DetailView
from django.http.response import HttpResponse
from accounts.models import Profile
from django.contrib.auth import views as auth_views

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
