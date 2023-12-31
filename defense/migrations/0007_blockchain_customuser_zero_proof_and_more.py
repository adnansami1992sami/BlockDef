# Generated by Django 4.2.1 on 2023-06-09 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('defense', '0006_alter_finalpapers_base_alter_finalpapers_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blockchain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_number', models.IntegerField()),
                ('previous_hash', models.CharField(max_length=64)),
                ('data', models.TextField()),
                ('hash', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='zero_proof',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='blockchain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='defense.blockchain'),
        ),
    ]
