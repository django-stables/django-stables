from django.db import models
from django.contrib.postgres.fields import JSONField


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    vcs_url = models.URLField(blank=False)


class Result(models.Model):
    project = models.ForeignKey('Project', db_index=True)
    installed_packages = JSONField()
    result = JSONField()


class Commit(models.Model):
    project = models.ForeignKey('Project', db_index=True)
    url = models.URLField(blank=False)


class Version(models.Model):
    project = models.ForeignKey('Project', db_index=True)
    version = models.CharField(max_length=50)


class ProjectStatus(models.Model):
    project = models.ForeignKey('Project', db_index=True)
    status = JSONField()
