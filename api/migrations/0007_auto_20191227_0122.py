# Generated by Django 3.0.1 on 2019-12-26 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20191225_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='value',
            field=models.TextField(),
        ),
    ]
