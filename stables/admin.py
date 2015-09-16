from django.contrib import admin
from stables import models

admin.site.register(models.Package)
admin.site.register(models.PackageVersion)
admin.site.register(models.Result)
admin.site.register(models.Commit)
