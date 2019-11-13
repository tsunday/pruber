from rest_framework.routers import SimpleRouter

from schedule.views import ReservationViewSet

router = SimpleRouter()
router.register(r'reservations', ReservationViewSet)

urlpatterns = router.urls
