# Generated by Django 3.2 on 2022-05-18 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0004_auto_20220518_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictedimage',
            name='category_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='predictedimage',
            name='category_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
