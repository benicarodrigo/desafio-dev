from django.urls import path
from .views import index, upload, operacao


urlpatterns = [
    path('', index, name='index'),
    path('upload/', upload, name='upload'),
    path('operacao/', operacao, name='operacao'),
]
