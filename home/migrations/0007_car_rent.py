# Generated by Django 3.1.7 on 2021-08-18 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210816_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='rent',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
