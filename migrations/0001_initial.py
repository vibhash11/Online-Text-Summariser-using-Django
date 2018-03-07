# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-06 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import sumbasic.val


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', sumbasic.val.ContentTypeRestrictedFileField(upload_to='./documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
