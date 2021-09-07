from django.urls import path

from .viewsets import UsersAPIView, FarmsAPIView, SeasonsAPIView

urlpatterns = [
    path('users/', UsersAPIView.as_view(), name='users'),
    path('farms/', FarmsAPIView.as_view(), name='farms'),
    path('seasons/', SeasonsAPIView.as_view(), name='seasons'),   
]