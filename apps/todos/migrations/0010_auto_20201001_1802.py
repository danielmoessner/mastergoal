# Generated by Django 2.2.16 on 2020-10-01 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0009_auto_20201001_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neverendingtodo',
            name='previous',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='todos.NeverEndingToDo'),
        ),
    ]
