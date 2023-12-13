from django.urls import path, include
from .views import save_user_info, get_user

urlpatterns = [
    path('save_info/', save_user_info),

    #path('get_info/', get_user),
    
]
