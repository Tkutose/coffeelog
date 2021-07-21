from django.urls import path
from . import views

app_name = 'coffeelog'

urlpatterns = [
    path('details/<int:pk>', views.LogDetail.as_view(), name='detail'),
]
