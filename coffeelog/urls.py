from django.urls import path
from . import views

app_name = 'coffeelog'

urlpatterns = [
    path('', views.LogList.as_view(), name='list'),
    path('details/<int:pk>', views.LogDetail.as_view(), name='detail'),
]
