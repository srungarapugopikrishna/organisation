# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 09:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
                ('father_or_husband_name', models.CharField(max_length=20)),
                ('nominee_name', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('job', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('mobile_no', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('share_amount', models.CharField(max_length=20)),
                ('loan_amount', models.CharField(max_length=20)),
                ('emi_amount', models.CharField(max_length=20)),
                ('no_of_emis', models.CharField(max_length=20)),
                ('rate_of_intrest', models.CharField(max_length=20)),
                ('intrest_amount', models.CharField(max_length=20)),
                ('total', models.CharField(max_length=20)),
                ('appid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appbill', to='people.Application')),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_amount', models.CharField(max_length=20)),
                ('balance', models.CharField(max_length=30)),
                ('billid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill', to='people.Bills')),
            ],
        ),
        migrations.CreateModel(
            name='SavingAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10)),
                ('share_amount', models.CharField(max_length=20)),
                ('balance', models.CharField(max_length=20)),
                ('appid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appacount', to='people.Application')),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('mobile_no', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
