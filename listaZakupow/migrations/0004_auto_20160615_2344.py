# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listaZakupow', '0003_auto_20160615_2338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lista',
            old_name='nazwa',
            new_name='title',
        ),
    ]
