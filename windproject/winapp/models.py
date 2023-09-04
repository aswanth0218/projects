from django.db import models

# Create your models here.
class windata(models.Model):
    valid_data = models.IntegerField()
    max_datapoint = models.IntegerField()
    active = models.BooleanField(default=True)

    def __del__(self):
        return self.name

class store_value(models.Model):
    find_value = models.IntegerField()

    class meta:
        db_table="data_availabity"
