from django.contrib import admin
from . models import Task, Project, ProjectGroup, Role, Permission
# Register your models here.

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(ProjectGroup)
admin.site.register(Role)
admin.site.register(Permission)



