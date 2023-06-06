from django.db import models

class NKUSTnews(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class cardata(models.Model):
    serial_number = models.IntegerField(default=0, blank=True) 
    accident_year_month = models.DateField(null=False,blank=False, help_text='事故年月')
    company_name = models.CharField(max_length=100, help_text='單位名稱')
    township = models.CharField(max_length=100, help_text='鄉鎮市區')
    death_toll = models.IntegerField(default=0, blank=True)
    Injured_umber = models.IntegerField(default=0, blank=True)
    weather_description = models.CharField(max_length=100)
    light_description = models.CharField(max_length=100)
    road_description = models.CharField(max_length=100)
    speed_limit = models.IntegerField(default=60, blank=True)
    description_of_road_type = models.CharField(max_length=100)
    description_of_road_conditions = models.CharField(max_length=100)
    description_of_pavement_defects = models.CharField(max_length=100)
    obstacle_description = models.CharField(max_length=100)
    accident_type_and_pattern = models.IntegerField(null=True)
    accident_type_and_description = models.CharField(max_length=100)
    surveillance_tape = models.CharField(max_length=100)

    class Meta:
        ordering = ('serial_number',)