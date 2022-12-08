from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products import data
from .models import *
from .serialize import *
from django.db.models import Q

# Get Routes
@api_view(['GET'])
def getRoutes(request):
    routes = [
    '/api/Product/',
    '/api/Food/',
    '/api/FineArt/',
    '/api/Interiors/',
    '/api/Events/',
    '/api/Films/',
    '/api/About/',
    '/api/Contact/',
    ]
    return Response(routes)

# Get Films YT Links
@api_view(['GET'])
def getFilms(request):
    filmListings = FilmsLinks.objects.order_by('-UploadDate').values()
    filmListingsFilter = filmListings.filter(Display_in_Products_Page__exact= True)
    return Response(filmListingsFilter)

# Get Product Pics
@api_view(['GET'])
def getProduct(request):
    productListings = ProductImages.objects.order_by('-UploadDate').all()
    productListingsFilter = ProductImageSerializer(productListings.filter(Display_in_Products_Page__exact= True), many=True)
    return Response(productListingsFilter.data)

# Get Food Pics
@api_view(['GET'])
def getFood(request):
    foodListings = FoodImages.objects.order_by('-UploadDate').all()
    foodListingsFilter = FoodImageSerializer(foodListings.filter(Display_in_Products_Page__exact= True), many=True)   
    return Response(foodListingsFilter.data)

# Get FineArt Pics
@api_view(['GET'])
def getFineArt(request):
    fineArtImagesListings = FineArtImages.objects.order_by('-UploadDate').all()
    fineArtImagesListingsFilter = FineArtImageSerializer(fineArtImagesListings.filter(Display_in_Products_Page__exact= True), many=True)   
    return Response(fineArtImagesListingsFilter.data)

# Get Interiors Pics by Category
@api_view(['GET'])
def getInteriors(request, pk):
    interorsImagesListings = InteriorsImages.objects.order_by('-UploadDate').all()
    interiorsImagesListingsFilter = InteriorsImageSerializer(interorsImagesListings.filter(Display_in_Products_Page__exact= True , SubCategory__exact = pk), many=True)      
    return Response(interiorsImagesListingsFilter.data)

# Get Events Pics by Category
@api_view(['GET'])
def getEvents(request, pk):
    eventsImagesListings = EventsImages.objects.order_by('-UploadDate').all()
    eventsImagesListingsFilter = EventsImageSerializer(eventsImagesListings.filter(Display_in_Products_Page__exact= True ,SubCategory__exact = pk), many=True)      
    return Response(eventsImagesListingsFilter.data)

# Get Weddings Pics by Category
@api_view(['GET'])
def getWeddings(request, pk):
    widdingImagesListings = WeddingImages.objects.order_by('-UploadDate').all()
    widdingImagesListingsFilter = WeddingsImageSerializer(widdingImagesListings.filter(Display_in_Products_Page__exact= True , SubCategory__exact = pk), many=True)      
    return Response(widdingImagesListingsFilter.data)

# Get Clientele 
@api_view(['GET'])
def getClientele(request):
    clienteleList = Clientele.objects.order_by('-UploadDate').all()
    clienteleListFilter = ClienteleListSerializer(clienteleList.filter(Display_in_Products_Page__exact= True), many=True)      
    return Response(clienteleListFilter.data)
    