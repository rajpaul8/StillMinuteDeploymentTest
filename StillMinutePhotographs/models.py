from django.db import models
from datetime import date
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# def file_size(value): # add this to some file where you can import it from
#     limit = 5 * 1024 * 1024
#     if value.size > limit:
#         raise ValidationError('File too large. Size should not exceed 5 MiB.')

class ProductImages(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Category = 'Product'
    Image = models.ImageField( default="")
    PictureName = models.CharField(max_length=200, default="", blank=True)
    PhotoGrapher = models.CharField(max_length=100, default="", blank=True)
    Date = models.DateField(default=date.today)
    Short_Description = models.CharField(max_length=500, default="", blank=True)
    Display_in_Products_Page = models.BooleanField(default=True)
    UploadDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.Name)

    class Meta:
        verbose_name_plural = "Product Images"



class FoodImages(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Category = 'Food'
    Image = models.ImageField( default="")
    PictureName = models.CharField(max_length=200, default="", blank=True)
    PhotoGrapher = models.CharField(max_length=100, default="", blank=True)
    Date = models.DateField(default=date.today)
    Short_Description = models.CharField(max_length=500, default="", blank=True)
    Display_in_Products_Page = models.BooleanField(default=True)
    UploadDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.Name)

    class Meta:
        verbose_name_plural = "Food Images"



class FineArtImages(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Category = 'FineArt'
    Image = models.ImageField( default="")
    PictureName = models.CharField(max_length=200, default="", blank=True)
    PhotoGrapher = models.CharField(max_length=100, default="", blank=True)
    Date = models.DateField(default=date.today)
    Short_Description = models.CharField(max_length=500, default="", blank=True)
    Display_in_Products_Page = models.BooleanField(default=True)
    UploadDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.Name)

    class Meta:
        verbose_name_plural = "Fine Art Images"



class InteriorsImages(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Category = 'Interiors'
    SubCategorySelection = (
        ('CommercialAndResidentialSpaces', 'Commercial And Residential Spaces'),
        ('InstallationArt', 'Installation Art'),
    )
    SubCategory = models.CharField(max_length=50, choices=SubCategorySelection, default="")
    Image = models.ImageField( default="")
    PictureName = models.CharField(max_length=200, default="", blank=True)
    PhotoGrapher = models.CharField(max_length=100, default="", blank=True)
    Date = models.DateField(default=date.today)
    Short_Description = models.CharField(max_length=500, default="", blank=True)
    Display_in_Products_Page = models.BooleanField(default=True)
    UploadDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.Name)

    class Meta:
        verbose_name_plural = "Interior Images"



class EventsImages(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Category = 'Events'
    SubCategorySelection = (
        ('MusicAndDance', 'Music And Dance'),
        ('EthnicEventsAndCelebrations', 'Ethnic Events And Celebrations'),
        ('CuratedEvents', 'Curated Events'),
    )
    SubCategory = models.CharField(max_length=50, choices=SubCategorySelection, default="")
    Image = models.ImageField( default="")
    PictureName = models.CharField(max_length=200, default="", blank=True)
    PhotoGrapher = models.CharField(max_length=100, default="", blank=True)
    Date = models.DateField(default=date.today)
    Short_Description = models.CharField(max_length=500, default="", blank=True)
    Display_in_Products_Page = models.BooleanField(default=True)
    UploadDate = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return str(self.Name)

    class Meta:
            verbose_name_plural = "Event Images"

class WeddingImages(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Category = 'Wedding'
    SubCategorySelection = (
        ('Candid', 'Candid'),
        ('FineArt', 'Fine Art'),
        ('Traditional', 'Traditional'),
        ('WeddingFilms', 'Wedding Films'),
    )
    SubCategory = models.CharField(max_length=50, choices=SubCategorySelection, default="")
    Image = models.ImageField( default="")
    PictureName = models.CharField(max_length=200, default="", blank=True)
    PhotoGrapher = models.CharField(max_length=100, default="", blank=True)
    Date = models.DateField(default=date.today)
    Short_Description = models.CharField(max_length=500, default="", blank=True)
    Display_in_Products_Page = models.BooleanField(default=True)
    UploadDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.Name)

    class Meta:
        verbose_name_plural = "Wedding Images"

class FilmsLinks(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    SubCategory = models.CharField(max_length=100, default="", blank=True)
    YoutubeEmbeddLink = models.CharField(max_length=800, default="")
    PictureName = models.CharField(max_length=200, default="", blank=True)
    PhotoGrapher = models.CharField(max_length=100, default="", blank=True)
    Short_Description = models.CharField(max_length=500, default="", blank=True)
    Display_in_Products_Page = models.BooleanField(default=True)
    UploadDate = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.Name)

    class Meta:
        verbose_name_plural = "Film Links"

class Clientele(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    Name = models.CharField(max_length=200, default="", blank=True)
    Image = models.ImageField( default="")
    UploadDate = models.DateTimeField(auto_now_add=True)
    Display_in_Products_Page = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.Name)

    class Meta:
        verbose_name_plural = "Clientele"