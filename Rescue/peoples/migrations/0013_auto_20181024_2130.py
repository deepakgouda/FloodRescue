# Generated by Django 2.1.2 on 2018-10-24 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoples', '0012_volunteers_personid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='need',
            field=models.CharField(choices=[('', '-------'), ('resuce', 'Need Rescue'), ('resource', 'Need Resources'), ('both', 'Need Resue and Resources')], default=' ', max_length=50),
        ),
    ]
