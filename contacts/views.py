from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import CustomUserChangeForm
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


class ContactFormView(FormView):
    form_class = CustomUserChangeForm
    template_name = 'contactform.html'
