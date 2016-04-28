# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('message', models.CharField(max_length=300)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('is_sent', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
