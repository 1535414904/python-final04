from django.db import models

class cardata(models.Model):
    serial_number = models.IntegerField() 
    accident_year_month = models.DateField(null=False,blank=False)
    company_name = models.CharField(max_length=100)
    township = models.CharField(max_length=100)
    death_toll = models.IntegerField()
    Injured_umber = models.IntegerField()
    weather_description = models.CharField(max_length=100)
    light_description = models.CharField(max_length=100)
    road_description = models.CharField(max_length=100)
    speed_limit = models.IntegerField()
    description_of_road_type = models.CharField(max_length=100)
    description_of_road_conditions = models.CharField(max_length=100)
    description_of_pavement_defects = models.CharField(max_length=100)
    obstacle_description = models.CharField(max_length=100)
    accident_type_and_pattern = models.IntegerField()
    accident_type_and_description = models.CharField(max_length=100)
    surveillance_tape = models.CharField(max_length=100)

    class Meta:
        ordering = ('serial_number',)
    def __str__(self):
        return self.serial_number
