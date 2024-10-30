# Generated by Django 5.1.2 on 2024-10-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='can_assign_tasks',
            field=models.BinaryField(default=False),
        ),
        migrations.AlterField(
            model_name='roles',
            name='can_comment',
            field=models.BinaryField(default=False),
        ),
        migrations.AlterField(
            model_name='roles',
            name='can_create_task',
            field=models.BinaryField(default=False),
        ),
        migrations.AlterField(
            model_name='roles',
            name='can_delete_task',
            field=models.BinaryField(default=False),
        ),
        migrations.AlterField(
            model_name='roles',
            name='can_edit_task',
            field=models.BinaryField(default=False),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='priority',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]