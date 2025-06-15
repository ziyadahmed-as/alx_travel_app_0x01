from rest_framework import serializers
from .models import Listing, Booking, Review

# listing serializer model
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

# booking serializer model
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

# reviewer serializer model
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('created_at', 'average_rating')