from django.db import models
from django.contrib.postgres.fields import JSONField


class Package(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    vcs_url = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class PackageVersion(models.Model):
    package = models.ForeignKey('Package', db_index=True)
    version = models.CharField(max_length=50)
    status = JSONField()

    def __str__(self):
        return '%s %s' % (self.package, self.version)


class Result(models.Model):
    package_version = models.ForeignKey('PackageVersion', db_index=True)
    installed_packages = JSONField()
    result = JSONField()
    commit_url = models.CharField(max_length=255, blank=False)


class Commit(models.Model):
    package = models.ForeignKey('Package', db_index=True)
    commit_url = models.CharField(max_length=255, blank=False)
