# Generated by Django 2.2.16 on 2020-10-21 16:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="neverendingtodo",
            name="previous",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="next",
                to="todos.NeverEndingToDo",
            ),
        ),
        migrations.AddField(
            model_name="pipelinetodo",
            name="previous",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="pipeline_to_dos",
                to="todos.ToDo",
            ),
        ),
        migrations.AddField(
            model_name="repetitivetodo",
            name="previous",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="next",
                to="todos.RepetitiveToDo",
            ),
        ),
        migrations.AddField(
            model_name="todo",
            name="user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="to_dos",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
