from coffeelog import views
from django.urls.conf import include
from django.urls import path
from rest_framework import routers
from public import views
app_name = 'public'


urlpatterns = [
    path('', views.TopView.as_view(), name="top")
]
