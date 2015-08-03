# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('vcs_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', django.contrib.postgres.fields.jsonb.JSONField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stables.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installed_packages', django.contrib.postgres.fields.jsonb.JSONField()),
                ('result', django.contrib.postgres.fields.jsonb.JSONField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stables.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stables.Project')),
            ],
        ),
        migrations.AddField(
            model_name='commit',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stables.Project'),
        ),
    ]
