from django.urls import path
from . import views

urlpatterns = [
    path('user/change/', views.profile_change, name='profile_change')
]
