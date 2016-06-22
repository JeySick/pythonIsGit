# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listaZakupow', '0004_auto_20160615_2344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lista',
            old_name='title',
            new_name='nazwa',
        ),
    ]
