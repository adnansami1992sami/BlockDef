# Generated by Django 4.2.1 on 2023-06-04 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defense', '0002_rename_subject_filecode_mission_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='base',
            field=models.CharField(choices=[('None', 'None'), ('Al Dafra Base', 'Al Dafra Base'), ('Al Tanf Base', 'Al Tanf Base')], default='None', max_length=40),
        ),
        migrations.AlterField(
            model_name='filecode',
            name='mission',
            field=models.CharField(max_length=30),
        ),
    ]
