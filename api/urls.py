from django.urls import path, include
from .views import save_user_info, index

urlpatterns = [
    path('', index, 'index'),
    path('save_info/', save_user_info),
]
