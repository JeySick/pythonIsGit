# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listaZakupow', '0002_lista'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lista',
            old_name='author',
            new_name='autor',
        ),
    ]
