from django.db import models

class cardata(models.Model):
    編號 = models.IntegerField(default=0)
    發生日期 = models.CharField(max_length=100)
    原因 = models.CharField(max_length=100)
    class Meta:
        ordering = ('編號',)
    def __int__(self):
        return self.編號
