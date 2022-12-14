# Generated by Django 4.1.3 on 2022-12-04 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StillMinutePhotographs', '0002_rename_clickedby_productimages_photographer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsImages',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('SubCategory', models.CharField(choices=[('MusicAndDance', 'Music And Dance'), ('EthnicEventsAndCelebrations', 'Ethnic Events And Celebrations'), ('CuratedEvents', 'Curated Events')], default='', max_length=50)),
                ('Image', models.ImageField(default='', upload_to='Images/%Y/%m/%d')),
                ('ProductName', models.CharField(blank=True, default='', max_length=200)),
                ('PhotoGrapher', models.CharField(blank=True, default='', max_length=100)),
                ('Date', models.DateField(default=datetime.date.today)),
                ('Short_Description', models.CharField(blank=True, default='', max_length=500)),
                ('Display_in_Products_Page', models.BooleanField(default=True)),
                ('UploadDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FineArtImages',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Image', models.ImageField(default='', upload_to='Images/%Y/%m/%d')),
                ('ProductName', models.CharField(blank=True, default='', max_length=200)),
                ('PhotoGrapher', models.CharField(blank=True, default='', max_length=100)),
                ('Date', models.DateField(default=datetime.date.today)),
                ('Short_Description', models.CharField(blank=True, default='', max_length=500)),
                ('Display_in_Products_Page', models.BooleanField(default=True)),
                ('UploadDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodImages',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Image', models.ImageField(default='', upload_to='Images/%Y/%m/%d')),
                ('ProductName', models.CharField(blank=True, default='', max_length=200)),
                ('PhotoGrapher', models.CharField(blank=True, default='', max_length=100)),
                ('Date', models.DateField(default=datetime.date.today)),
                ('Short_Description', models.CharField(blank=True, default='', max_length=500)),
                ('Display_in_Products_Page', models.BooleanField(default=True)),
                ('UploadDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InteriorsImages',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('SubCategory', models.CharField(choices=[('CommercialAndResidential', 'Commercial And Residential'), ('InstallationArt', 'Installation Art')], default='', max_length=50)),
                ('Image', models.ImageField(default='', upload_to='Images/%Y/%m/%d')),
                ('ProductName', models.CharField(blank=True, default='', max_length=200)),
                ('PhotoGrapher', models.CharField(blank=True, default='', max_length=100)),
                ('Date', models.DateField(default=datetime.date.today)),
                ('Short_Description', models.CharField(blank=True, default='', max_length=500)),
                ('Display_in_Products_Page', models.BooleanField(default=True)),
                ('UploadDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeddingImages',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('SubCategory', models.CharField(choices=[('Candid', 'Candid'), ('FineArt', 'Fine Art'), ('Traditional', 'Traditional'), ('WeddingFilms', 'Wedding Films')], default='', max_length=50)),
                ('Image', models.ImageField(default='', upload_to='Images/%Y/%m/%d')),
                ('ProductName', models.CharField(blank=True, default='', max_length=200)),
                ('PhotoGrapher', models.CharField(blank=True, default='', max_length=100)),
                ('Date', models.DateField(default=datetime.date.today)),
                ('Short_Description', models.CharField(blank=True, default='', max_length=500)),
                ('Display_in_Products_Page', models.BooleanField(default=True)),
                ('UploadDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
