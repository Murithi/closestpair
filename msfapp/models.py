from django.db import models

# Create your models here.
class ClosePairs(models.Model):
  submitted_points = models.CharField(max_length=4000)
  closest_pair = models.CharField(max_length=50)
  timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)

