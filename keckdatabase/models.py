from django.db import models
from django.urls import reverse

class Object(models.Model):
    obj_id = models.IntegerField(primary_key=True, blank=True)
    name = models.TextField(blank=True, null=True)
    ra = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=4)  # This field type is a guess.
    dec = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=4)  # This field type is a guess.
    champion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('object-detail', args=[str(self.obj_id)])

    class Meta:
        managed = False
        db_table = 'Object'

class Measurements(models.Model):
    obj = models.OneToOneField('Object', primary_key=True, on_delete=models.CASCADE, blank=True)
    mtype = models.TextField(blank=True, null=True)
    distance = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)  # This field type is a guess.
    gaiadistance = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=2)  # This field type is a guess.
    sptype = models.TextField(blank=True, null=True)
    propermotion = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    vmag = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    bminusv = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.obj)

    class Meta:
        managed = False
        db_table = 'Measurements'


class Observations(models.Model):
    obj = models.OneToOneField('Object', primary_key=True, on_delete=models.CASCADE, blank=True)
    followup = models.BooleanField(blank=True, null=True)
    candidates = models.IntegerField(blank=True, null=True)
    reductionnotes = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.obj)

    class Meta:
        managed = False
        db_table = 'Observations'
