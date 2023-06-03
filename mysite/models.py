from django.db import models

class cardata(models.Model):
    serial_number = models.IntegerField(default=0)
    date_of_occurrence = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
    class Meta:
        ordering = ('編號',)
    def __str__(self):
        return self.serial_number
