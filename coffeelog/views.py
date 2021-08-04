from django.urls import reverse
from django.views import generic
from django.db.models import Count
from .models import Log, Store
from .forms import LogForm

# Create your views here.

class LogDetail(generic.DetailView):
    '''
    Logの詳細を表示
    '''
    template_name = 'coffeelog/log_detail.html'
    model = Log
    context_object_name = 'log'

    # 選択した商品と同じ店舗の商品を取得
    def get_context_data(self, **kwargs):
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

    def get_form(self):
        form = super(LogCreate, self).get_form()
        form.fields['store'].label = '店名'
        form.fields['store'].label = '店名'
        form.fields['product'].label = '商品名'
        form.fields['price'].label = '価格'
        form.fields['hot'].label = 'hotならチェック'
        form.fields['bitter'].label = '苦味'
        form.fields['acidity'].label = '酸味'
        form.fields['smell'].label = '香り'
        form.fields['after'].label = '後味'
        form.fields['likely'].label = '個人的な好み'
        form.fields['note'].label = '備考'
        return form

    def get_context_data(self, **kwargs):
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

    def get_form(self):
        form = super(LogUpdate, self).get_form()
        form.fields['store'].label = '店名'
        form.fields['store'].label = '店名'
        form.fields['product'].label = '商品名'
        form.fields['price'].label = '価格'
        form.fields['hot'].label = 'hotならチェック'
        form.fields['bitter'].label = '苦味'
        form.fields['acidity'].label = '酸味'
        form.fields['smell'].label = '香り'
        form.fields['after'].label = '後味'
        form.fields['likely'].label = '個人的な好み'
        form.fields['note'].label = '備考'
        return form

    def get_context_data(self, **kwargs):
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
        該当する店ごとのLog投稿数をカウント,dict型でcountsに格納
        '''
        context = super().get_context_data(**kwargs)
        context['counts'] = {}
        for store in Store.objects.annotate(count = Count('log')):
            context['counts'][store.name] = store.count
        return context
