# Generated by Django 5.1.2 on 2024-10-25 08:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagement', '0010_alter_task_due_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='Assigned to',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Assigned by',
        ),
        migrations.AlterField(
            model_name='activitylog',
            name='user_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='permission',
            name='user_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='task',
            name='Project',
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_user_id_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='assigned_user', to=settings.AUTH_USER_MODEL, verbose_name='Assigned to'),
        ),
        migrations.AddField(
            model_name='task',
            name='project_id_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='taskmanagement.project', verbose_name='Project'),
        ),
        migrations.AddField(
            model_name='task',
            name='reporter_id_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='assignee', to=settings.AUTH_USER_MODEL, verbose_name='Assigned by'),
        ),
        migrations.DeleteModel(
            name='ToolUser',
        ),
    ]