from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rooms.views import RoomViewSet, AvailableRoomViewSet

router = DefaultRouter()
router.register(r'all', RoomViewSet)
router.register(r'available', AvailableRoomViewSet)

urlpatterns = [
    path('', include(router.urls))
]
