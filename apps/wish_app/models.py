from __future__ import unicode_literals

from django.db import models
from ..login_and_reg_app.models import User
# Create your models here.
class MyWishlist(models.Model):
    item_name = models.CharField(max_length=45)
    added_by = models.CharField(max_length=45)
    owner = models.CharField(max_length=45, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Biglist(models.Model):
    item_name = models.CharField(max_length=45)
    added_by = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
