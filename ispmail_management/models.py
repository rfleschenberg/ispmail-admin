from __future__ import unicode_literals

from django.db import models


class VirtualAliases(models.Model):
    domain = models.ForeignKey('VirtualDomains', models.DO_NOTHING)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'virtual_aliases'


class VirtualDomains(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'virtual_domains'


class VirtualUsers(models.Model):
    domain = models.ForeignKey(VirtualDomains, models.DO_NOTHING)
    password = models.CharField(max_length=150)
    email = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'virtual_users'
        unique_together = (('domain', 'email'),)
