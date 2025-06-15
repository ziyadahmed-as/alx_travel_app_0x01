from rest_framework import serializers
from .models import Listing, Booking, Review

# listing serializer model
class ListingSerializer(serializers.ModelSerializer):
    # This serializer handles the serialization of Listing model instances.
    # It includes all fields from the model and marks 'created_at' and 'updated_at' as read-only.
    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

# booking serializer model
class BookingSerializer(serializers.ModelSerializer):
    """ This serializer handles the serialization of Booking model instances."""
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

# reviewer serializer model
class ReviewSerializer(serializers.ModelSerializer):
    """ This serializer handles the serialization of Review model instances."""
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('created_at', 'average_rating')