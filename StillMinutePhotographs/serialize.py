from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'

class FoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodImages
        fields = '__all__'

class FineArtImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FineArtImages
        fields = '__all__'

class EventsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsImages
        fields = '__all__'

class InteriorsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteriorsImages
        fields = '__all__'

class WeddingsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeddingImages
        fields = '__all__'

class ClienteleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientele
        fields = '__all__'        