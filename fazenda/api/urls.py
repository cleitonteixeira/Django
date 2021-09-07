from django.urls import path

from .viewsets import UsersAPIView, FarmsAPIView, SeasonsAPIView, UserAPIView, FarmAPIView, SeasonAPIView

urlpatterns = [
    path('users/', UsersAPIView.as_view(), name='users'),
    path('users/<int:pk>/', UserAPIView.as_view(), name='user'),
    path('farms/', FarmsAPIView.as_view(), name='farms'),
    path('farms/<int:pk>/', FarmAPIView.as_view(), name='farm'),
    path('seasons/', SeasonsAPIView.as_view(), name='seasons'),
    path('seasons/<int:pk>/', SeasonAPIView.as_view(), name='season'),
]