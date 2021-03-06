# Generated by Django 4.0.5 on 2022-06-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.IntegerField(default=0)),
                ('place', models.CharField(blank=True, choices=[('thika', 'thika'), ('kiambu', 'kiambu'), ('mombasa', 'mombasa'), ('nairobi', 'nairobi'), ('nakuru', 'nakuru'), ('makadimu', 'makadimu'), ('mombasa', 'mombasa'), ('nairobi', 'nairobi'), ('makuyu', 'makuyu'), ('muranga', 'muranga'), ('Nyeri', 'Nyeri')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Laundry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
