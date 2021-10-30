"""passman URL Configuration

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

from django.conf import settings
from django.contrib import admin
from django.urls import path,include
import debug_toolbar
from mainApp.views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'passwordManager', PasswordManagerViewSet,basename='passwordManager')
router.register(r'password', PasswordViewSet,basename='password')


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('admin/', ),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include(router.urls)),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/', include('djoser.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

