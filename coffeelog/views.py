from django.urls import reverse
from django.views import generic
from django.db.models import Count
from django.http import Http404
from .models import Log, Store
from .forms import LogForm, StoreForm

# Create your views here.

class LogDetail(generic.DetailView):
    '''
    Logの詳細を表示
    '''
    template_name = 'coffeelog/log_detail.html'
    model = Log
    context_object_name = 'log'

    def get_context_data(self, **kwargs):
        '''
        選択した商品と同じ店舗の商品を取得
        '''
        context = super().get_context_data(**kwargs)
        obj = context.get('object')
        context['other'] = Log.objects.filter(store__name=obj.store).exclude(id=obj.id)
        return context


class LogList(generic.ListView):
    '''
    Logの一覧を表示
    '''
    template_name = 'coffeelog/log_list.html'
    model = Log
    context_object_name = 'log_list'


class LogCreate(generic.CreateView):
    '''
    新規Log投稿
    '''
    template_name = 'coffeelog/log_form.html'
    form_class = LogForm
    model = Log

    def get_context_data(self, **kwargs):
        '''
        createとupdateで同じtemplateを使うので、表示部分の切り替え
        '''
        context = super().get_context_data(**kwargs)
        context['title'] = '新規Log投稿'
        context['btn'] = 'Add Log'
        return context

    def get_success_url(self):
        return reverse('coffeelog:detail', kwargs={'pk': self.object.id})


class LogUpdate(generic.UpdateView):
    '''
    Logの更新
    '''
    template_name = 'coffeelog/log_form.html'
    form_class = LogForm
    model = Log

    def get_context_data(self, **kwargs):
        '''
        createとupdateで同じtemplateを使うので、表示部分の切り替え
        '''
        context = super().get_context_data(**kwargs)
        context['title'] = 'Log更新'
        context['btn'] = 'Update'
        return context

    def get_success_url(self):
        return reverse('coffeelog:detail', kwargs={'pk': self.object.id})


class StoreList(generic.ListView):
    '''
    Logの投稿されている店一覧を表示
    '''
    template_name = 'coffeelog/store_list.html'
    model = Store
    context_object_name = 'store_list'

    def get_context_data(self, **kwargs):
        '''
        該当する店ごとのLog投稿数をカウントし、dict型でcountsに格納
        '''
        context = super().get_context_data(**kwargs)
        context['counts'] = {}
        for store in Store.objects.annotate(count = Count('log')):
            context['counts'][store.name] = store.count
        return context


class StoreCreate(generic.CreateView):
    '''
    店の新規登録
    '''
    template_name = 'coffeelog/store_form.html'
    form_class = StoreForm
    model = Store

    def get_success_url(self):
        return reverse('coffeelog:new')


class SearchList(generic.ListView):
    '''
    指定されたキーワードで絞込み検索を行い、結果を表示する
    '''
    template_name = 'coffeelog/search_list.html'
    model = Log


    def get_context_data(self, **kwargs):
        '''
        type:並び替えならsort、絞り込みならnarrow
        col:列名
        target:条件
        '''
        context = super().get_context_data(**kwargs)
        type = self.request.GET['type']
        col = self.request.GET['col']
        target = self.request.GET['target']
        context['col'] = col
        try:
            if(type=='narrow'):
                context['results'] = Log.objects.filter(**{col: target})
                context['kind'] = ':{}の絞り込み結果'.format(target)

            elif(target=='asc'):
                context['results'] = Log.objects.order_by(col)
                context['kind'] = 'の並び替え結果(昇順)'

            elif(target=='desc'):
                context['results'] = Log.objects.order_by(col).reverse()
                context['kind'] = 'の並び替え結果(降順)'

        except ValueError:
            raise Http404("検索結果が見つかりませんでした。")

        return context
