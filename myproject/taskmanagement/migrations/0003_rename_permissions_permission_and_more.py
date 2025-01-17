# Generated by Django 5.1.2 on 2024-10-24 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagement', '0002_alter_roles_can_assign_tasks_alter_roles_can_comment_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Permissions',
            new_name='Permission',
        ),
        migrations.RenameModel(
            old_name='ProjectGroups',
            new_name='ProjectGroup',
        ),
        migrations.RenameModel(
            old_name='Roles',
            new_name='Role',
        ),
        migrations.RenameModel(
            old_name='ActivityLogs',
            new_name='ActivityLog',
        ),
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
        migrations.RenameModel(
            old_name='ToolUsers',
            new_name='ToolUser',
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=20)),
                ('priority', models.CharField(max_length=20)),
                ('due_date', models.TimeField()),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('updated_at', models.TimeField()),
                ('assigned_user_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assigned_user', to='taskmanagement.tooluser')),
                ('project_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='taskmanagement.project')),
                ('reporter_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assignee', to='taskmanagement.tooluser')),
            ],
        ),
        migrations.AlterField(
            model_name='activitylog',
            name='task_id_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='taskmanagement.task'),
        ),
        migrations.DeleteModel(
            name='Tasks',
        ),
    ]
