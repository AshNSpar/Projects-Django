# Generated by Django 3.2.7 on 2021-09-29 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0007_alter_myuser_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
