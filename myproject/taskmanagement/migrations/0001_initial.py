# Generated by Django 5.1.2 on 2024-10-16 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('can_create_task', models.BinaryField()),
                ('can_edit_task', models.BinaryField()),
                ('can_delete_task', models.BinaryField()),
                ('can_comment', models.BinaryField()),
                ('can_assign_tasks', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='ToolUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('project_group_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='taskmanagement.projectgroups')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('status', models.IntegerField()),
                ('priority', models.IntegerField()),
                ('due_date', models.TimeField()),
                ('created_at', models.TimeField()),
                ('updated_at', models.TimeField()),
                ('project_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='taskmanagement.projects')),
                ('assigned_user_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assigned_user', to='taskmanagement.toolusers')),
                ('reporter_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assignee', to='taskmanagement.toolusers')),
            ],
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='taskmanagement.projects')),
                ('role_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='taskmanagement.roles')),
                ('user_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='taskmanagement.toolusers')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=1)),
                ('timestamp', models.TimeField()),
                ('task_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='taskmanagement.tasks')),
                # task / project : id 
                ('user_id_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='taskmanagement.toolusers')),
            ],
        ),
    ]
