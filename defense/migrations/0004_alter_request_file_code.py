# Generated by Django 4.2.1 on 2023-06-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defense', '0003_alter_customuser_base_alter_filecode_mission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='file_code',
            field=models.CharField(default='None', max_length=70),
        ),
    ]
