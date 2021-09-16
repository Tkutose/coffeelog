from functools import partial
from django_filters import filterset, rest_framework as filters
from django.contrib.auth import login
from rest_framework.fields import Field
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from coffeelog.serializers import LogSerializer, LogListSerializer, OnlyCoffeeDataSeriarizer, StoreSerializer, UserLogSerializer, UserLogListSerializer
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.views import generic
from django.db.models import Count, fields
from django.http import Http404, response
from django.shortcuts import get_object_or_404
from coffeelog.models import Log, Store, UserLog
from coffeelog.forms import LogForm, StoreForm
from rest_framework import status, views, viewsets
from rest_framework.response import Response

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
        other:選択した商品と同じ店舗の商品を取得
        userlog:その商品の投稿された記録を取得
        '''
        context = super().get_context_data(**kwargs)
        obj = context.get('object')
        context['other'] = Log.objects.filter(store__name=obj.store).exclude(id=obj.id)
        context['user_log'] = UserLog.objects.filter(product=obj.id)
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


"""
DRF View

CRUDに対して
SELECT:GET
INSERT:POST
UPDATE:PUT/PATCH
DELETE:DELETE
のハンドラがそれぞれ対応している
"""

class LogFilter(filters.FilterSet):
    """Logモデル用filter"""
    # 商品名で検索
    name = filters.CharFilter(field_name="product",lookup_expr='icontains')
    
    class Meta:
        model = Log
        fields = '__all__'

class LogListAPIView(views.APIView):
    """Logクラスの一覧取得APIView"""
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = LogFilter

    def get(self, request, *args, **kwargs):
        """一覧取得APIに対するハンドラ"""

        filterset = LogFilter(request.query_params, queryset=Log.objects.all() )
        if not filterset.is_valid():
            # バリデートでエラーが発生した場合
            raise ValidationError(filterset.errors)

        # シリアライザオブジェクトを生成(manyでListを指定することも可能)
        serializer = LogListSerializer(instance=filterset.qs)
        # serializer = LogSerializer(instance=filterset.qs, many=True)

        # responseを返す
        return Response(serializer.data, status.HTTP_200_OK)


class LogAPIView(views.APIView):
    """Logクラスの情報取得APIView"""

    def get(self, request, pk, *args, **kwargs):
        """情報取得APIに対するハンドラ(pkの引数付きで呼び出し)"""

        log = get_object_or_404(Log, pk=pk)
        Serializer = LogSerializer(instance=log)
        return Response(Serializer.data, status.HTTP_200_OK)


class LogUpdateAPIView(views.APIView):

    def patch(self, request, pk, *args, **kwargs):
        """Logの一部更新（感想部分のみ）を行うAPIView"""

        log = get_object_or_404(Log, pk=pk)

        # requestしたdataで、Logの一部更新を行う
        serializer = LogSerializer(instance=log, data=request.data, partial=True)
        
        # バリデート(感想部分以外はread_only)
        serializer.is_valid(raise_exception=True)

        # 一部更新
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class StoreAPIView(views.APIView):
    """Storeクラスの情報取得APIView"""


    def get(self, request, pk, *args, **kwargs):
        """Storeクラスの情報取得APIに対するハンドラ(pkの引数付きで呼び出し)"""

        store = get_object_or_404(Store, pk=pk)
        Serializer = StoreSerializer(instance=store)
        return Response(Serializer.data, status.HTTP_200_OK)


class OnlyCoffeeAPIViewSet(viewsets.ReadOnlyModelViewSet):
    """Logのコーヒーの情報だけを取得するAPIViewSet(read_only)"""

    queryset = Log.objects.all()
    serializer_class = OnlyCoffeeDataSeriarizer



class UserLogFilter(filters.FilterSet):
    """UserLogモデル用filter"""

    class Meta:
        model = UserLog
        fields = '__all__'

class UserLogListAPIView(views.APIView):
    """UserLogクラスの一覧取得APIView"""

    def get(self, request, *args, **kwargs):
        """一覧取得APIに対するハンドラ"""

        filterset = UserLogFilter(request.query_params, queryset=UserLog.objects.all() )
        if not filterset.is_valid():
            # バリデートでエラーが発生した場合
            raise ValidationError(filterset.errors)

        # シリアライザオブジェクトを生成(manyでListを指定することも可能)
        serializer = UserLogListSerializer(instance=filterset.qs)
        # serializer = UserLogSerializer(instance=filterset.qs, many=True)

        # responseを返す
        return Response(serializer.data, status.HTTP_200_OK)


class UserLogAPIView(views.APIView):
    """UserLogクラスの情報取得APIView"""

    def get(self, request, pk, *args, **kwargs):
        """情報取得APIに対するハンドラ(pkの引数付きで呼び出し)"""

        user_log = get_object_or_404(UserLog, pk=pk)
        Serializer = UserLogSerializer(instance=user_log)
        return Response(Serializer.data, status.HTTP_200_OK)
