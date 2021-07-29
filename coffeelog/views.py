from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Log, Store

# Create your views here.

class LogDetail(generic.DetailView):
    model = Log
    context_object_name = 'log'

    # 選択した商品と同じ店舗の商品を取得
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context.get('object')
        log = Log.objects.filter(store__store=obj.store).exclude(id=obj.id)
        context['other'] = "まだ登録されていませんでした" if not log else log
        return context


class LogList(generic.ListView):
    model = Log
    context_object_name = 'log_list'


    # 選択した商品と同じ店舗の商品を取得
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stores'] = Store.objects.all()
        return context
