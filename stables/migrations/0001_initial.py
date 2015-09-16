# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commit_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('vcs_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='PackageVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=50)),
                ('status', django.contrib.postgres.fields.jsonb.JSONField()),
                ('package', models.ForeignKey(to='stables.Package')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installed_packages', django.contrib.postgres.fields.jsonb.JSONField()),
                ('result', django.contrib.postgres.fields.jsonb.JSONField()),
                ('commit_url', models.URLField()),
                ('package_version', models.ForeignKey(to='stables.PackageVersion')),
            ],
        ),
        migrations.AddField(
            model_name='commit',
            name='package',
            field=models.ForeignKey(to='stables.Package'),
        ),
    ]
