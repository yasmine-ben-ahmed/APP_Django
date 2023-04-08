from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.gis.db import models
from signup.models import client
from signup.models import supervisor

from django.contrib.gis.geos import Point
from location_field.models.plain import PlainLocationField


class myProject(models.Model):
    nomp = models.CharField(max_length=50, null=True)
    geomp = models.PolygonField(null=True)
    descp = models.TextField(null=True)
    debutp = models.DateTimeField(default=timezone.now,null=True)
    finp = models.DateTimeField(null=True)
    cityp = models.CharField(max_length=255,null=True)
    locationp = PlainLocationField(based_fields=['cityp'], zoom=7,null=True)
    clientp = models.ForeignKey(client, on_delete=models.CASCADE,null=True)
    
    
    def __str__(self):
        return f' Project: {self.nomp}'