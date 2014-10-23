from django.db import models

# The Module class
class Module(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    code = models.CharField(max_length=6)
    desc_length = models.IntegerField()
