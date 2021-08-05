from django.urls import path
from . import views

app_name = 'coffeelog'

urlpatterns = [
    path('', views.LogList.as_view(), name='list'),
    path('detail/<int:pk>', views.LogDetail.as_view(), name='detail'),
    path('new/', views.LogCreate.as_view(), name='new'),
    path('new/store', views.StoreCreate.as_view(), name='new_store'),
    path('update/<int:pk>', views.LogUpdate.as_view(), name='update'),
    path('store/', views.StoreList.as_view(), name='store'),
    path('search/', views.SearchList.as_view(), name='search'),
]
