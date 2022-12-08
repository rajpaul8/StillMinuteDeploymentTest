from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('Product/', views.getProduct, name="Product"),
    path('Food/', views.getFood, name="Food"),
    path('FineArt/', views.getFineArt, name="FineArt"),
    path('Interiors/<str:pk>', views.getInteriors, name="Interiors"),
    path('Events/<str:pk>', views.getEvents, name="Events"),
    path('Weddings/<str:pk>', views.getWeddings, name="Weddings"),
    path('Films/', views.getFilms, name="Films"),
    path('About/Clientele', views.getClientele, name="About"),
]