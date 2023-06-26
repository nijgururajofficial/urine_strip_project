from django.db import models

from django.db import models

class UrineStrip(models.Model):
    image = models.ImageField(upload_to='urine_strips/')
    colors = models.JSONField()
    