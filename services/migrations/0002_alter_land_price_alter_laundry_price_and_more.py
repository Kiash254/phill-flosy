# Generated by Django 4.0.5 on 2022-06-30 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='laundry',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]
