from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=300)
    established_date = models.IntegerField()
    description = models.TextField()
