# Generated by Django 3.2.6 on 2022-01-14 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madmin', '0003_alter_adddevice_imei_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddevice',
            name='imei_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='adddevice',
            name='primary_sim',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='adddevice',
            name='secondary_sim',
            field=models.CharField(max_length=10),
        ),
    ]
