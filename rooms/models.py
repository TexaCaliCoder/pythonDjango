from django.db import models

# Create your models here.
class Room(models.Model):
    coordinates = models.CharField(help_text='use literal _eval() to convert string to tuple', max_length=25)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    n = models.IntegerField(default = -1)
    s = models.IntegerField(default = -1)
    e = models.IntegerField(default = -1)
    w = models.IntegerField(default = -1)