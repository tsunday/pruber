from django.contrib import admin

from bands.models import Band


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    pass
