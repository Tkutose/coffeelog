from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Log

# Create your views here.


class LogDetail(generic.DetailView):
    model = Log
    context_object_name = 'log'