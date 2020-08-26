from django.urls import path

from . import views


urlpatterns = [
    path('', views.upload_image_view, name='upload_image_view'),
]
