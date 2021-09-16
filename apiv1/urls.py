from coffeelog import views
from django.db import router
from django.urls.conf import include
from django.urls import path
from rest_framework import routers
from . import views
app_name = 'apiv1'

# router = routers.DefaultRouter()
# router.register('', views.OnlyCoffeeAPIViewSet)

urlpatterns = [
    # path('coffee', include(router.urls)),
    path('api/new', views.UserLogCreateAPIView.as_view(), name="user-log_new")
]
