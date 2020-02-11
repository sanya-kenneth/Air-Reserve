from django.urls import path
from .views import FlightsView, ListFlightsView,\
    EditFlight, RetrieveFlight


urlpatterns = [
    path('flights/all/', ListFlightsView.as_view(), name="list_flights"),
    path('flights/', FlightsView.as_view(), name="create_flights"),
    path('flights/<int:pk>', RetrieveFlight.as_view(), name="retrieve_flight"),
    path('flights/<int:pk>/update', EditFlight.as_view(), name="edit_flight")
]
