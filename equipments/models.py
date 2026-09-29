from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    register_number = models.IntegerField()
    register_date = models.DateField()

    def __str__(self):
        return self.name
