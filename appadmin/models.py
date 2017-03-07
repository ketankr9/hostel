from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DhanrajHostel(models.Model):
    room_no = models.IntegerField(primary_key=True)
    a = models.CharField(db_column='A', max_length=10, blank=True, null=True)  # Field name made lowercase.
    b = models.CharField(db_column='B', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dhanraj_hostel'
