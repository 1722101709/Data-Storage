from django.db import models

# Create your models here.

class Dst(models.Model):
    class Meta:
        app_label = "data_storage_App"
        managed = True
    name = models.CharField(max_length=87)
    age = models.IntegerField()
    area = models.CharField(max_length=117)
    gender = models.CharField(max_length=11)
