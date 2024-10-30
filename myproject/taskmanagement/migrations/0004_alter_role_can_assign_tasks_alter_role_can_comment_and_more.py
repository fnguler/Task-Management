# Generated by Django 5.1.2 on 2024-10-24 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagement', '0003_rename_permissions_permission_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='can_assign_tasks',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='role',
            name='can_comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='role',
            name='can_create_task',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='role',
            name='can_delete_task',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='role',
            name='can_edit_task',
            field=models.BooleanField(default=False),
        ),
    ]
