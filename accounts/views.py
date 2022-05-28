from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomCreatUserForm


class SignUp(generic.CreateView):
    form_class = CustomCreatUserForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


