from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Log

# Create your views here.

class LogDetail(generic.DetailView):
    model = Log
    context_object_name = 'log'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context.get('object')
        log = Log.objects.filter(store__store=obj.store).exclude(id=obj.id)
        context['other'] = "まだ登録されていませんでした" if not log else log
        return context
