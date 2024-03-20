"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.templates import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.templates'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp3.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('les1/', include('myapp.urls')),
    path('les2/', include('myapp2.urls')),
    path('les3/', include('myapp3.urls')),
    path('', index),
    path('h2/', include('homework2.urls')),
    path('les4/', include('myapp4.urls')),
    # path('__debug__/', include("debug_toolbar.urls")),
    path('les6/', include('myapp6.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
