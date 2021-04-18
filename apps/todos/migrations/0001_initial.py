# Generated by Django 2.2.16 on 2020-10-21 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('activate', models.DateTimeField(blank=True, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('completed', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('DONE', 'Done'), ('FAILED', 'Failed')], default='ACTIVE', max_length=20)),
            ],
            options={
                'ordering': ('is_archived', 'deadline', 'status', 'activate', 'name'),
            },
        ),
        migrations.CreateModel(
            name='NeverEndingToDo',
            fields=[
                ('todo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='todos.ToDo')),
                ('duration', models.DurationField()),
                ('blocked', models.BooleanField(default=False)),
            ],
            bases=('todos.todo',),
        ),
        migrations.CreateModel(
            name='NormalToDo',
            fields=[
                ('todo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='todos.ToDo')),
            ],
            bases=('todos.todo',),
        ),
        migrations.CreateModel(
            name='PipelineToDo',
            fields=[
                ('todo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='todos.ToDo')),
            ],
            bases=('todos.todo',),
        ),
        migrations.CreateModel(
            name='RepetitiveToDo',
            fields=[
                ('todo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='todos.ToDo')),
                ('duration', models.DurationField()),
                ('repetitions', models.PositiveSmallIntegerField(default=None, null=True)),
            ],
            bases=('todos.todo',),
        ),
    ]