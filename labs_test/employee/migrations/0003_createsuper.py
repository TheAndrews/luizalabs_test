
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.admin import User


def create_superuser(apps, schema_editor):
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'admin'
    superuser.email = 'admin@admin.net'
    superuser.set_password('admin')
    superuser.save()


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20190526_1703'),
    ]

    operations = [
        migrations.RunPython(create_superuser)
    ]