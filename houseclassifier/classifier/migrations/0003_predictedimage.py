# Generated by Django 3.2 on 2022-05-18 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0002_rename_image_pre_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='predicted_image')),
                ('category_name', models.CharField(max_length=50)),
                ('category_id', models.IntegerField()),
            ],
        ),
    ]
