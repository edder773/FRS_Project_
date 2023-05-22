from django.urls import path
from .views import CustomUserView

urlpatterns = [
    path('accounts/user/', CustomUserView.as_view(), name='custom_user'),
]
