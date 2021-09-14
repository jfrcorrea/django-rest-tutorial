from django.db import models


class ChuckNorrisJoke(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    url = models.URLField()
    value = models.CharField(max_length=500)
