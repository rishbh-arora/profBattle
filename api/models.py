from django.db import models
from django.core.validators import MaxValueValidator
class Faculty(models.Model):
    name = models.CharField(max_length=40)
    role = models.CharField(max_length=75)
    department = models.CharField(max_length=75)
    publications = models.PositiveIntegerField()
    strict = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    skill = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    marks = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    fit = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    ap = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    link = models.URLField(null=True, blank=True)