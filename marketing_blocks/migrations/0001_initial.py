# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-04-25 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketingBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
                ('position', models.CharField(choices=[('header', 'header'), ('footer', 'footer')], default='header', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
