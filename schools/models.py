from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=300)
    established_date = models.IntegerField()
    description = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
