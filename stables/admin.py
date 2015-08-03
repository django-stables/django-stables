from django.contrib import admin
from stables import models

admin.site.register(models.Project)
admin.site.register(models.Result)
admin.site.register(models.Commit)
admin.site.register(models.ProjectStatus)
