from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', views.OnlyCoffeeAPIViewSet)

app_name = 'coffeelog'



urlpatterns = [
    path('', views.LogList.as_view(), name='list'),
    path('detail/<int:pk>', views.LogDetail.as_view(), name='detail'),
    path('new/', views.LogCreate.as_view(), name='new'),
    path('new/store', views.StoreCreate.as_view(), name='new_store'),
    path('update/<int:pk>', views.LogUpdate.as_view(), name='update'),
    path('store/', views.StoreList.as_view(), name='store'),
    path('search/', views.SearchList.as_view(), name='search'),
    
    # API
    # リスト取得
    path('api/log/', views.LogListAPIView.as_view(), name="api_log_list"),
    # 詳細取得
    path('api/log/<int:pk>', views.LogAPIView.as_view(), name="api_log_detail"),

    # 試しで作ったため、ルーティングから除外
    # path('api/log/update/<int:pk>', views.LogUpdateAPIView.as_view(), name="api_log_update"),

    path('api/store/<int:pk>', views.StoreAPIView.as_view(), name="api_store_detail"),
    path('api/coffee/', include(router.urls)),   
]
