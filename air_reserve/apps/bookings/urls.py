from django.urls import path
from .views import CreateBookingsView, ListBookingsView, \
    RetrieveBooking, CancelBooking


urlpatterns = [
    path('bookings/', ListBookingsView.as_view(), name="list_bookings"),
    path('flights/<int:pk>/bookings/', CreateBookingsView.as_view(), name="book_flight"),
    path('bookings/<int:pk>', RetrieveBooking.as_view(), name="retrieve_booking"),
    path('bookings/<int:pk>/cancel', CancelBooking.as_view(), name="cancel_booking")
]
