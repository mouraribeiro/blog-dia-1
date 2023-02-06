
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

# Create your views here.
class SingUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'login'

