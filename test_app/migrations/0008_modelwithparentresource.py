# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-11-28 04:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0007_auto_20180816_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelWithParentResource',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text_field', models.CharField(blank=True, max_length=32, null=True)),
                ('basic_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.BasicClass')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
