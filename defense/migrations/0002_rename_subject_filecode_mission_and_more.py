# Generated by Django 4.2 on 2023-04-17 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defense', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filecode',
            old_name='subject',
            new_name='mission',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mission',
            field=models.CharField(choices=[('None', 'None'), ('security', 'security')], default='None', max_length=30),
        ),
    ]
