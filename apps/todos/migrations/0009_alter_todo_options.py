# Generated by Django 4.2.16 on 2024-10-28 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0008_alter_todo_options_alter_todo_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ('status', '-completed', 'name', 'deadline', 'activate')},
        ),
    ]
