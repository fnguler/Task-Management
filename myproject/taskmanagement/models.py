from django.db import models
from django.forms import SelectDateWidget

# Create your models here.

class ProjectGroup(models.Model):
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    can_create_task = models.BooleanField(default=False)
    can_edit_task = models.BooleanField(default=False)
    can_delete_task = models.BooleanField(default=False)
    can_comment = models.BooleanField(default=False)
    can_assign_tasks = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.TextField()
    project_group_id_fk = models.ForeignKey('taskmanagement.ProjectGroup', on_delete=models.PROTECT)
    
    def __str__(self):
        return self.title

class Permission(models.Model):
    user_id_fk = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    role_id_fk= models.ForeignKey('taskmanagement.Role', on_delete=models.PROTECT)
    project_id_fk = models.ForeignKey('taskmanagement.Project', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.user_id_fk} as {self.role_id_fk} for {self.project_id_fk}"
    
class Task(models.Model):
    title = models.TextField()
    description = models.TextField()
    project_id_fk = models.ForeignKey('taskmanagement.Project', on_delete=models.PROTECT, verbose_name="Project", null=True)
    assigned_user_id_fk = models.ForeignKey('auth.User',related_name='assigned_user', on_delete=models.PROTECT, verbose_name="Assigned to", null=True)
    reporter_id_fk = models.ForeignKey('auth.User', related_name='assignee', on_delete=models.PROTECT, verbose_name="Assigned by", null=True)
    status = models.CharField(max_length=20, choices=[('todo', 'Todo'), ('in-progress', 'In Progress'), ('done', 'Done')])
    priority = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    due_date = models.DateField(null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    

class ActivityLog(models.Model):
    task_id_fk = models.ForeignKey('taskmanagement.Task', on_delete=models.PROTECT)
    user_id_fk = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    action = models.CharField(max_length=1)
    timestamp = models.TimeField()
