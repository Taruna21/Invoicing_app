# Generated by Django 2.1 on 2022-10-30 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20221030_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='province',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
