# Generated by Django 2.2.4 on 2019-08-07 22:03

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('page_choice', models.CharField(choices=[('DASHBOARD', 'Dashboard View'), ('TO_DOS', "To Do's View"), ('TREE', 'Tree View'), ('STAR', 'Star View'), ('NOTES', 'Notes View')], default='DASHBOARD', max_length=10)),
                ('goal_depth', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('goal_choice', models.CharField(choices=[('ALL', 'Show all goals.'), ('STAR', 'Show all starred goals.'), ('UNREACHED', 'Show all not yet achieved goals.'), ('ACHIEVED', 'Show all achieved goals.'), ('DEPTH', 'Show all goals within the depth range.'), ('NONE', 'Show no goals.')], default='ALL', max_length=10)),
                ('progress_monitor_choice', models.CharField(choices=[('ALL', 'Show all progress monitors.'), ('UNREACHED', 'Show all not yet fully loaded progress monitors.'), ('LOADED', 'Show all fully loaded progress monitors.'), ('RELATED', 'Show goal related progress monitors.'), ('NONE', 'Show no progress monitors.')], default='ALL', max_length=10)),
                ('link_choice', models.CharField(choices=[('ALL', 'Show all links.'), ('RELATED', 'Show master or sub goal related links.'), ('XRELATED', 'Show master and sub goal related links.'), ('NONE', 'Show no links.')], default='ALL', max_length=10)),
                ('strategy_choice', models.CharField(choices=[('ALL', 'Show all strategies.'), ('STAR', 'Show all starred strategies.'), ('RELATED', 'Show goal related strategies.'), ('NONE', 'Show no strategies.')], default='ALL', max_length=10)),
                ('starview_todos_delta', models.DurationField(blank=True, default=datetime.timedelta(days=7))),
                ('starview_normaltodos_choice', models.CharField(choices=[('ALL', "Show all to do's."), ('ACTIVE', "Show all active to do's"), ('UNFINISHED', "Show all unfinished to do's"), ('DELTA', 'Show all to dos that are active and with a deadline within the delta range.'), ('OVERDUE', 'Show all to dos that are overdue.'), ('ORANGE', 'Show all to dos that are active or orange or red.'), ('RELATED', 'Show goal related to dos.'), ('NONE', "Show no to do's.")], default='ALL', max_length=10)),
                ('starview_repetitivetodos_choice', models.CharField(choices=[('ALL', "Show all to do's."), ('ACTIVE', "Show all active to do's"), ('UNFINISHED', "Show all unfinished to do's"), ('DELTA', 'Show all to dos that are active and with a deadline within the delta range.'), ('OVERDUE', 'Show all to dos that are overdue.'), ('ORANGE', 'Show all to dos that are active or orange or red.'), ('RELATED', 'Show goal related to dos.'), ('NONE', "Show no to do's.")], default='ALL', max_length=10)),
                ('starview_neverendingtodos_choice', models.CharField(choices=[('ALL', "Show all to do's."), ('ACTIVE', "Show all active to do's"), ('UNFINISHED', "Show all unfinished to do's"), ('DELTA', 'Show all to dos that are active and with a deadline within the delta range.'), ('OVERDUE', 'Show all to dos that are overdue.'), ('ORANGE', 'Show all to dos that are active or orange or red.'), ('RELATED', 'Show goal related to dos.'), ('NONE', "Show no to do's.")], default='ALL', max_length=10)),
                ('starview_multipletodos_choice', models.CharField(choices=[('ALL', "Show all to do's."), ('ACTIVE', "Show all active to do's"), ('UNFINISHED', "Show all unfinished to do's"), ('DELTA', 'Show all to dos that are active and with a deadline within the delta range.'), ('OVERDUE', 'Show all to dos that are overdue.'), ('ORANGE', 'Show all to dos that are active or orange or red.'), ('RELATED', 'Show goal related to dos.'), ('NONE', "Show no to do's.")], default='ALL', max_length=10)),
                ('starview_pipelinetodos_choice', models.CharField(choices=[('ALL', "Show all to do's."), ('ACTIVE', "Show all active to do's"), ('UNFINISHED', "Show all unfinished to do's"), ('DELTA', 'Show all to dos that are active and with a deadline within the delta range.'), ('OVERDUE', 'Show all to dos that are overdue.'), ('ORANGE', 'Show all to dos that are active or orange or red.'), ('RELATED', 'Show goal related to dos.'), ('NONE', "Show no to do's.")], default='ALL', max_length=10)),
                ('to_dos_delta', models.DurationField(blank=True, default=datetime.timedelta(days=7))),
                ('normal_to_dos_choice', models.CharField(choices=[('ALL', "Show all to do's."), ('ACTIVE', "Show all active to do's"), ('UNFINISHED', "Show all unfinished to do's"), ('DELTA', 'Show all to dos that are active and with a deadline within the delta range.'), ('OVERDUE', 'Show all to dos that are overdue.'), ('ORANGE', 'Show all to dos that are active or orange or red.'), ('RELATED', 'Show goal related to dos.'), ('NONE', "Show no to do's.")], default='ALL', max_length=10)),
                ('repetitive_to_dos_choice', models.CharField(choices=[('ALL', "Show all to do's."), ('ACTIVE', "Show all active to do's"), ('UNFINISHED', "Show all unfinished to do's"), ('DELTA', 'Show all to dos that are active and with a deadline within the delta range.'), ('OVERDUE', 'Show all to dos that are overdue.'), ('ORANGE', 'Show all to dos that are active or orange or red.'), ('RELATED', 'Show goal related to dos.'), ('NONE', "Show no to do's.")], default='ALL', max_length=10)),
                ('never_ending_to_dos_choice', models.CharField(choices=[('ALL', "Show all to do's."), ('ACTIVE', "Show all active to do's"), ('UNFINISHED', "Show all unfinished to do's"), ('DELTA', 'Show all to dos that are active and with a deadline within the delta range.'), ('OVERDUE', 'Show all to dos that are overdue.'), ('ORANGE', 'Show all to dos that are active or orange or red.'), ('RELATED', 'Show goal related to dos.'), ('NONE', "Show no to do's.")], default='ALL', max_length=10)),
                ('multiple_to_dos_choice', models.CharField(choices=[('ALL', "Show all to do's."), ('ACTIVE', "Show all active to do's"), ('UNFINISHED', "Show all unfinished to do's"), ('DELTA', 'Show all to dos that are active and with a deadline within the delta range.'), ('OVERDUE', 'Show all to dos that are overdue.'), ('ORANGE', 'Show all to dos that are active or orange or red.'), ('RELATED', 'Show goal related to dos.'), ('NONE', "Show no to do's.")], default='ALL', max_length=10)),
                ('pipeline_to_dos_choice', models.CharField(choices=[('ALL', "Show all to do's."), ('ACTIVE', "Show all active to do's"), ('UNFINISHED', "Show all unfinished to do's"), ('DELTA', 'Show all to dos that are active and with a deadline within the delta range.'), ('OVERDUE', 'Show all to dos that are overdue.'), ('ORANGE', 'Show all to dos that are active or orange or red.'), ('RELATED', 'Show goal related to dos.'), ('NONE', "Show no to do's.")], default='ALL', max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]