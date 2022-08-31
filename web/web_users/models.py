from django.core import signing
from django.db import models


# Create your models here.
from firstapp.models import SystemUser


class Countries(models.Model):
    name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=10, default=None, null=True)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_signed_pk(self):
        return signing.dumps(self.pk)

    class Meta:
        db_table = 'countries'
