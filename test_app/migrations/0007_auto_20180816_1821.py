# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-08-16 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0006_auto_20180515_0618'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelWithSensitiveData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('basic_text', models.CharField(blank=True, max_length=32, null=True)),
                ('top_secret', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='basicclass',
            name='model_with_sensitive_data',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_app.ModelWithSensitiveData'),
        ),
    ]
