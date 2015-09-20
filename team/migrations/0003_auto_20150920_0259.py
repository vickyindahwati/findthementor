# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_materi_mentor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('materi', models.ForeignKey(to='team.Materi')),
                ('mentor', models.ForeignKey(to='team.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='materi',
        ),
        migrations.DeleteModel(
            name='Mentor',
        ),
        migrations.AddField(
            model_name='materi',
            name='category',
            field=models.CharField(default=django.utils.datetime_safe.date.today, max_length=10, choices=[(b'BACKEND', b'Backend'), (b'FRONTEND', b'Frontend')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=datetime.date(2015, 9, 20), max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(default=datetime.date(2015, 9, 20), max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_mentee',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_mentor',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
