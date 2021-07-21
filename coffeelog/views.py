from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Log

# Create your views here.

class Index(TemplateView):
    template_name = 'coffeelog/index.html'

    
class LogList(ListView):
    model = Log
    context_object_name = 'log_list'

    # １ページに表示する件数
    paginate_by = 10

    def get_queryset(self):
        logs = Log.objects.all().order_by('date')
        return logs
