from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

# Create your views here.
class ClientSideView(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'client_side.html'
    paginate_by = 100

class ServerSideView(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'server_side.html'
    paginate_by = 5

class LazyLoadView(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'lazy_load.html'
    paginate_by = 10
    ordering = ['id']