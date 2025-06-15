from django.urls import path, include
from .views import ListingListCreateView, BookingListCreateView
from .views import ListingViewSet, BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('listings/', ListingListCreateView.as_view(), name='listing-list-create'),
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('api/', include(router.urls)),
]