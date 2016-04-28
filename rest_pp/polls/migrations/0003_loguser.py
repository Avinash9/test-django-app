# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160428_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogUser',
            fields=[
                ('id', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('logs', models.ForeignKey(to='polls.Logs')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
