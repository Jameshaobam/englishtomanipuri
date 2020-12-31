from django.db import models


class EnglishToManipuri(models.Model):

    English = models.CharField(max_length=300)
    Manipuri = models.CharField(max_length=300)

    def __str__(self):
        return self.English