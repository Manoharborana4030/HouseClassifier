# Generated by Django 3.2 on 2022-05-18 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0003_predictedimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pre_Image',
        ),
        migrations.AlterField(
            model_name='predictedimage',
            name='img',
            field=models.ImageField(upload_to='predicted_images'),
        ),
    ]
