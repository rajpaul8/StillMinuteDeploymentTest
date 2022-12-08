from django.contrib import admin
from .models import *

class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('PictureName', 'PhotoGrapher', 'UploadDate', 'Display_in_Products_Page',)
    list_filter = ('PhotoGrapher', 'Display_in_Products_Page')
    search_fields = ('PictureName', 'PhotoGrapher', 'UploadDate', 'Display_in_Products_Page',)
    list_per_page = 20

admin.site.register(ProductImages, ProductImagesAdmin)
class FoodImagesAdmin(admin.ModelAdmin):
    list_display = ('PictureName', 'PhotoGrapher', 'UploadDate', 'Display_in_Products_Page',)
    list_filter = ('PhotoGrapher', 'Display_in_Products_Page')
    search_fields = ('PictureName', 'PhotoGrapher', 'UploadDate', 'Display_in_Products_Page',)
    list_per_page = 20

admin.site.register(FoodImages, FoodImagesAdmin)

class FineArtImagesAdmin(admin.ModelAdmin):
    list_display = ('PictureName', 'PhotoGrapher', 'UploadDate', 'Display_in_Products_Page',)
    list_filter = ('PhotoGrapher', 'Display_in_Products_Page')
    search_fields = ('PictureName', 'PhotoGrapher', 'UploadDate', 'Display_in_Products_Page',)
    list_per_page = 20

admin.site.register(FineArtImages, FineArtImagesAdmin)

class InteriorsImageAdmin(admin.ModelAdmin):
    list_display = ('SubCategory', 'PictureName', 'PhotoGrapher', 'UploadDate', 'Display_in_Products_Page',)
    list_filter = ('SubCategory', 'PhotoGrapher', 'Display_in_Products_Page')
    search_fields = ('SubCategory', 'PictureName', 'PhotoGrapher', 'UploadDate', 'Display_in_Products_Page',)
    list_per_page = 20

admin.site.register(InteriorsImages, InteriorsImageAdmin)

class EventsImagesAdmin(admin.ModelAdmin):
    list_display = ('SubCategory', 'PictureName', 'PhotoGrapher', 'UploadDate', 'Display_in_Products_Page',)
    list_filter = ('SubCategory', 'PhotoGrapher', 'Display_in_Products_Page')
    search_fields = ('SubCategory', 'PictureName', 'PhotoGrapher', 'UploadDate', 'Display_in_Products_Page',)
    list_per_page = 20

admin.site.register(EventsImages, EventsImagesAdmin)


class WeddingsImagesAdmin(admin.ModelAdmin):
    list_display = ('SubCategory','PictureName', 'PhotoGrapher', 'UploadDate', 'Display_in_Products_Page',)
    list_filter = ('SubCategory','PhotoGrapher', 'Display_in_Products_Page')
    search_fields = ('SubCategory','PictureName', 'PhotoGrapher', 'UploadDate', 'Display_in_Products_Page',)
    list_per_page = 20

admin.site.register(WeddingImages, WeddingsImagesAdmin)

class FilmsLinksAdmin(admin.ModelAdmin):
    list_display = ('YoutubeEmbeddLink', 'UploadDate', 'PhotoGrapher', 'Display_in_Products_Page',)
    list_filter = ('SubCategory','PhotoGrapher', 'UploadDate','Display_in_Products_Page')
    search_fields = ('SubCategory','PictureName', 'UploadDate','PhotoGrapher', 'Display_in_Products_Page',)
    list_per_page = 20

admin.site.register(FilmsLinks, FilmsLinksAdmin)

class ClienteleAdmin(admin.ModelAdmin):
    list_display = ('Image', 'UploadDate', 'Name', 'Display_in_Products_Page',)
    list_filter = ('Image', 'UploadDate', 'Name', 'Display_in_Products_Page',)
    search_fields = ('Image', 'UploadDate', 'Name', 'Display_in_Products_Page',)
    list_per_page = 20

admin.site.register(Clientele, ClienteleAdmin)
