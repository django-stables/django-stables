# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commit',
            name='commit_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='package',
            name='vcs_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='result',
            name='commit_url',
            field=models.CharField(max_length=255),
        ),
    ]
