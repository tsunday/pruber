from django.contrib import admin

from schedule.models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass
