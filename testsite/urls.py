"""testsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),

    # vue.jsを使ったページ
    path('', include('public.urls')),

    # Djangoと情報取得API
    path('coffeelog/', include('coffeelog.urls')),

    # 管理者以外のLog投稿用API
    path('userlog/', include('apiv1.urls')),

    # ログインページ(Djangoデフォルト)
    path('login/',  views.LoginView.as_view(), name='login'),

    #APIリファレンス
    # path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    # path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    # path('api/schema/redoc/', SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    ]
