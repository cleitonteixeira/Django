from django.urls import path

from rest_framework.routers import SimpleRouter

from .viewsets import ( 
    FarmsAPIView, 
    SeasonsAPIView,
    FarmAPIView, 
    SeasonAPIView,
    FarmViewSet,
    SeasonViewSet,
    UserAddViewSet
    )


router = SimpleRouter()
router.register('farms', FarmViewSet)
router.register('seasons', SeasonViewSet)
router.register('create-user', UserAddViewSet)


urlpatterns = [
    path('farms/', FarmsAPIView.as_view(), name='farms'),
    path('farms/<int:pk>/', FarmAPIView.as_view(), name='farm'),
    path('farms/<int:farm_pk>/seasons/', SeasonsAPIView.as_view(), name='seasons'),
    path('farms/<int:farm_pk>/seasons/<int:season_pk>', SeasonAPIView.as_view(), name='season'),
    
    path('seasons/', SeasonsAPIView.as_view(), name='seasons'),
    path('seasons/<int:season_pk>/', SeasonAPIView.as_view(), name='season'),
]