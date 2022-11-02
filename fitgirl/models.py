from django.db import models

# Create your models here.
class Games(models.Model):
    name = models.CharField
    fitgirl  = models.ForeignKey(null=True)
    steamunlk = models.ForeignKey(null=True)