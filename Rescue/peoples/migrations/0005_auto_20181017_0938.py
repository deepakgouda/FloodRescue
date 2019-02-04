# Generated by Django 2.0.3 on 2018-10-17 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoples', '0004_auto_20181017_0638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=30)),
                ('district', models.CharField(choices=[('', '-------'), ('Dist1', 'Dist1'), ('Dist2', 'Dist2'), ('Dist3', 'Dist3'), ('Dist4', 'Dist4'), ('Dist5', 'Dist5')], default=' ', max_length=50)),
                ('phone_no', models.IntegerField(blank=True, default=9993993287)),
                ('organisation', models.CharField(blank=True, default='', max_length=30)),
                ('area_of_volunteering', models.CharField(choices=[('', '-------'), ('dcr', 'Doctor'), ('elw', 'Electrical Works'), ('vls', 'Vehicle Support'), ('rlo', 'Relief operation'), ('cln', 'Cleaning'), ('bot', 'Boat Service'), ('oth', 'Other')], default=' ', max_length=50)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='person_email_link',
        ),
        migrations.RemoveField(
            model_name='person',
            name='person_img',
        ),
        migrations.RemoveField(
            model_name='person',
            name='person_phone_no',
        ),
        migrations.RemoveField(
            model_name='person',
            name='person_user',
        ),
        migrations.RemoveField(
            model_name='person',
            name='username',
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.TextField(blank=True, max_length=150, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Age'),
        ),
        migrations.AddField(
            model_name='person',
            name='district',
            field=models.CharField(blank=True, choices=[('', '-------'), ('Dist1', 'Dist1'), ('Dist2', 'Dist2'), ('Dist3', 'Dist3'), ('Dist4', 'Dist4'), ('Dist5', 'Dist5')], max_length=15, null=True, verbose_name='Residence District'),
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(0, 'Male'), (1, 'Female'), (2, 'Others')], null=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default='', max_length=51, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Mobile'),
        ),
    ]