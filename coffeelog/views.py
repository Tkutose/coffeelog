from django.urls import reverse
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
    success_url = '/details/'

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

    def get_success_url(self):
        return reverse('coffeelog:detail', kwargs={'pk': self.object.id})
