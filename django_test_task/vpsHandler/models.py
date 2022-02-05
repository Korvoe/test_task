from django.db import models

class VPS(models.Model):
    uid = models.CharField(primary_key=True, max_length=12)
    cpu = models.PositiveIntegerField()
    ram = models.PositiveIntegerField()
    hdd = models.PositiveIntegerField()
    status = models.CharField(max_length=7)

    def __str__(self):
        return self.uid
