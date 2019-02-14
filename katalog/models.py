from django.db.models import CharField
from django.db.models import TextField
from django.db.models import FileField
from django.db.models import ImageField
from django.utils import timezone
from django.db import models as models

# Create your models here.

class Katalog(models.Model):
    model_pic = models.ImageField(upload_to='')
    name = models.CharField(max_length=100)
    harga = models.CharField(max_length=100)

    def __str__(self):
        return self.name
