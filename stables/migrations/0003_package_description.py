# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stables', '0002_auto_20150804_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
