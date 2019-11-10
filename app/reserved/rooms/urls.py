from django.urls import path, include
from rest_framework.routers import SimpleRouter

from rooms.views import RoomViewSet

router = SimpleRouter()
router.register(r'', RoomViewSet)

urlpatterns = [
    path('', include(router.urls))
]
