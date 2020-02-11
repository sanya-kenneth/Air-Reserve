from .serializers import FlightsSerializer
from .models import Flights
from air_reserve.apps.helpers.utilities import find_missing_fields
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, \
    UpdateAPIView, RetrieveAPIView


class FlightsView(CreateAPIView):
    """
    View class for creating flights
    """
    serializer_class = FlightsSerializer

    def create(self, request):
        required_fields = ['departing_from', 'destination', 'date_of_departure',
                           'departure_time', 'fee']
        data = {}
        if not request.user.is_superuser:
            return Response({
                            'error': 'You are not allowed to perform this action'},
                            status=status.HTTP_403_FORBIDDEN)
        validate_request = find_missing_fields(request.data, required_fields)
        if validate_request['error'] != 'None':
            return Response({'error': validate_request['error']}, status=400)
        data['departing_from'] = request.data.get('departing_from')
        data['destination'] = request.data.get('destination')
        data['date_of_departure'] = request.data.get('date_of_departure')
        data['departure_time'] = request.data.get('departure_time')
        data['fee'] = request.data.get('fee')
        serializer = FlightsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = serializer.data
        return Response({
            'data': response_data,
            'message': 'flight created successfuly',
            'success': True
        }, status=201)


class ListFlightsView(ListAPIView):
    """
    View class to handle fetch all requests for flights
    """
    authentication_classes = ()
    serializer_class = FlightsSerializer
    queryset = Flights.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'data': serializer.data, 'success': True})


class RetrieveFlight(RetrieveAPIView):
    authentication_classes = ()
    serializer_class = FlightsSerializer
    queryset = Flights.objects.all()

    def get(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'data': serializer.data, 'success': True},
                        status=status.HTTP_200_OK)


class EditFlight(UpdateAPIView):
    """
    View class to handle updating and deleting
    a flight
    """
    serializer_class = FlightsSerializer
    queryset = Flights.objects.all()

    def update(self, request, pk, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({
                            'error': 'You are not allowed to perform this action'},
                            status=status.HTTP_403_FORBIDDEN)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        no_changes_msg = "no changes were made."
        if request.data:
            data = request.data
            if str(data["departing_from"]) == str(instance.departing_from) and \
                    str(data["destination"]) == str(instance.destination) and \
                    str(data["date_of_departure"]) == str(instance.date_of_departure) and \
                    str(data["departure_time"][0:4]) == str(instance.departure_time)[1:5]:
                return Response({'message': no_changes_msg})
            serializer = self.get_serializer(instance, data=request.data,
                                             partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({
                'data': serializer.data,
                'success': True,
                'message': 'flight data was updated'})
        return Response({'message': no_changes_msg})
