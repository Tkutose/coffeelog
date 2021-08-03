from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Log, Store
from .forms import LogForm

# Create your views here.

class LogDetail(generic.DetailView):
    template_name = 'coffeelog/log_detail.html'
    model = Log
    context_object_name = 'log'

    # 選択した商品と同じ店舗の商品を取得
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context.get('object')
        context['other'] = Log.objects.filter(store__store=obj.store).exclude(id=obj.id)
        return context


class LogList(generic.ListView):
    template_name = 'coffeelog/log_list.html'
    model = Log
    context_object_name = 'log_list'


    # 選択した商品と同じ店舗の商品を取得
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stores'] = Store.objects.all()
        return context

class LogCreate(generic.CreateView):
    template_name = 'coffeelog/log_new.html'
    form_class = LogForm
    model = Log
    success_url = '/details/1'

