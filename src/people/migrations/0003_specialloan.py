# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-05 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20171107_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special_loan_amout', models.IntegerField(default=0)),
                ('special_intrest_amount', models.IntegerField(default=0)),
                ('special_intrest_rate', models.FloatField(default=0.0)),
                ('appid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='appsploan', to='people.Application')),
            ],
        ),
    ]
