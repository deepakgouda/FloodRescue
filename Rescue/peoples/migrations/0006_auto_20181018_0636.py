# Generated by Django 2.0.3 on 2018-10-18 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoples', '0005_auto_20181017_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='aadhar',
            field=models.IntegerField(blank=True, null=True, verbose_name='Aadhar'),
        ),
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.IntegerField(blank=True, null=True, verbose_name='status'),
        ),
    ]