from django.db import models

class Band(models.Model):
    phone = models.PositiveIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['phone', 'name'], name='unique_band')
        ]