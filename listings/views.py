from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filterset_fields = ['location', 'price', 'amenities']
    search_fields = ['title', 'description']

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filterset_fields = ['listing', 'user', 'start_date', 'end_date']
    search_fields = ['user__username']

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer