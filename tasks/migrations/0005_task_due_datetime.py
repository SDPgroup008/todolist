# Generated by Django 4.1.7 on 2023-05-27 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_task_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]