# Generated by Django 3.0.1 on 2019-12-25 17:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191224_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='posting_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
