from django.urls import path, include
from .views import save_user_info

urlpatterns = [
    path('save_info/', save_user_info),
]
