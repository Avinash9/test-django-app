# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_loguser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loguser',
            name='logs',
        ),
        migrations.AddField(
            model_name='logs',
            name='logs',
            field=models.ForeignKey(default=1, to='polls.LogUser'),
            preserve_default=False,
        ),
    ]
