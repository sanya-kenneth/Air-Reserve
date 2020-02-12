from .serializers import BookingsSerializer
from .models import Bookings
from air_reserve.apps.flights.models import Flights
from air_reserve.apps.helpers.utilities import find_missing_fields
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, \
    UpdateAPIView, RetrieveAPIView


class CreateBookingsView(CreateAPIView):
    """
    View class for creating bookings
    """
    serializer_class = BookingsSerializer

    def create(self, request, pk):
        data = {}
        if request.user.is_superuser:
            return Response({
                            'error': 'You are not allowed to perform this action'},
                            status=status.HTTP_403_FORBIDDEN)
        try:
            flight = Flights.objects.get(pk=pk)
        except Flights.DoesNotExist:
            return Response({
                'message': 'flight does not exist',
                'success': False}, status=status.HTTP_404_NOT_FOUND)
        data['user'] = request.user.id
        data['flight'] = flight.id
        serializer = BookingsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = serializer.data
        response_data["user_email"] = request.user.email
        return Response({
            'data': response_data,
            'message': 'flight booked successfuly',
            'success': True
        }, status=201)


class ListBookingsView(ListAPIView):
    """
    View class to handle fetch all requests for bookings
    """
    serializer_class = BookingsSerializer

    def list(self, request):
        queryset = Bookings.objects.filter(
            user=request.user.id, booking_cancelled=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response({'data': serializer.data, 'success': True})


class RetrieveBooking(RetrieveAPIView):

    serializer_class = BookingsSerializer
    queryset = Bookings.objects.all()

    def get(self, request, pk):
        instance = self.get_object()
        user = request.user 
        if instance.booking_cancelled or instance.user.id != user.id:
            return Response({
                'message': 'booking not found'}, status=status.HTTP_404_NOT_FOUND)
        flight_data = {
            'departing_from': instance.flight.departing_from,
            'destination': instance.flight.destination,
            'date_of_departure': instance.flight.date_of_departure,
            'departure_time': instance.flight.departure_time,
            'fee': instance.flight.fee,
            'id': instance.flight.id
        }
        user_data = {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone_number': user.phone_number,
            'id': user.id
        }
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['flight'] = flight_data
        data['user'] = user_data
        return Response({'data': data, 'success': True},
                        status=status.HTTP_200_OK)


class CancelBooking(UpdateAPIView):
    
    serializer_class = BookingsSerializer
    queryset = Bookings.objects.all()
    
    def update(self, request, pk, *args, **kwargs):
        if request.user.is_superuser:
            return Response({
                            'error': 'You are not allowed to perform this action'},
                            status=status.HTTP_403_FORBIDDEN)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.booking_cancelled is False and instance.user.id == request.user.id:
            data = {'booking_cancelled': True}
            serializer = self.get_serializer(instance, data=data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({
                'success': True,
                'message': 'your flight booking was cancelled'})
        return Response({'message': 'booking not found'})
