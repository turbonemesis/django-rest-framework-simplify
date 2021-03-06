# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-12-10 03:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import rest_framework_simplify.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicClass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('active', models.BooleanField(default=True)),
                ('exclude_field', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChildClass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EncryptedClass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('encrypted_val', rest_framework_simplify.fields.SimplifyEncryptedCharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LinkingClass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('basic_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linking_classes', to='test_app.BasicClass')),
                ('child_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linking_classes', to='test_app.ChildClass')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MetaDataClass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('choice', models.CharField(choices=[('one', 'One'), ('two', 'Two'), ('three', 'Three')], default='two', max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='basicclass',
            name='child_one',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basic_class_one', to='test_app.ChildClass'),
        ),
        migrations.AddField(
            model_name='basicclass',
            name='child_three',
            field=models.ManyToManyField(blank=True, null=True, related_name='basic_class_three', to='test_app.ChildClass'),
        ),
        migrations.AddField(
            model_name='basicclass',
            name='child_two',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basic_class_two', to='test_app.ChildClass'),
        ),
    ]
