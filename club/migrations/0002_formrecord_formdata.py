# Generated by Django 5.1 on 2024-08-22 00:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.formfield')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.formmodel')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.formrecord')),
            ],
        ),
    ]
