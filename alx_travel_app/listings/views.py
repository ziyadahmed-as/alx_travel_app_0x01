from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
# This view provides `list` and `create` actions for the Listing model with filtering and searching capabilities.
class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filterset_fields = ['location', 'price', 'amenities']
    search_fields = ['title', 'description']
# This view provides `list` and `create` actions for the Booking model with filtering and searching capabilities.
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filterset_fields = ['listing', 'user', 'start_date', 'end_date']
    search_fields = ['user__username']
# This viewset provides `list` and `create` actions for the Listing model with filtering and searching capabilities.
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

# This viewset provides default `list`, `create`, `retrieve`, `update`, and `destroy` actions for the Listing model.
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer