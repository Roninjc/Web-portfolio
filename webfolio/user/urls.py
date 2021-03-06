"""user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from . import views

urlpatterns = [
    path('<str:mode>/delete/<int:pk>/', views.delete_obj, name='delete-obj'),
    path('imup', views.upload_image, name='upload-image'),
    path('tacr', views.create_tags, name='create-tag'),
    path('', views.user_panel, name='user-panel'),
    path('logout', views.logout, name='logout'),
]
