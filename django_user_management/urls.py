"""django_user_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views

EXCLUDED_APPS = (

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('logout/', views.LogoutView.as_view(), name='logout')
    #path('', include('social_django.urls', namespace='social'))
]


urlpatterns += [
    path('', include('{app}.urls'.format(app=app))) for app in settings.INSTALLED_APPS
    if app.startswith('django_user_management.apps') and app not in EXCLUDED_APPS
]
