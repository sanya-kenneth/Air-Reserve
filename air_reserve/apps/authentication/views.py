from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from air_reserve.apps.helpers.utilities import find_missing_fields
from .serializers import SignupUserSerializer,\
    SignupAdminSerializer


required_fields = ["first_name", "last_name", "email", "phone_number",
                           "password"]


class SignupUser(CreateAPIView):
    """
    view class for signing up a new user with the normal
    user role
    """
    serializer_class = SignupUserSerializer
    
    def create(self, request):
        """
        Method creates a new user with the normal user role
        """
        data = {}
        validate_request = find_missing_fields(request.data, required_fields)
        if validate_request['error'] != 'None':
            return Response({'error': validate_request['error']}, status=400)
        data['first_name'] = request.data.get('first_name')
        data['last_name'] = request.data.get('last_name')
        data['email'] = request.data.get('email')
        data['phone_number'] = request.data.get('phone_number')
        data['password'] = request.data.get('password')
        serializer = SignupUserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = serializer.data
        return Response({
            'data': response_data,
            'message': 'account created successfuly',
            'success': True 
            }, status=201)


class SignupAdmin(CreateAPIView):
    """
    View class for creating users with the admin role
    """
    serializer_class = SignupAdminSerializer
    
    def create(self, request):
        """
        Method creates a new user with the admin user role
        """
        data = {}
        data['email'] = request.data.get('email')
        data['first_name'] = request.data.get('first_name')
        data['last_name'] = request.data.get('last_name')
        data['phone_number'] = request.data.get('phone_number')
        data['password'] = request.data.get('password')
        serializer = SignupAdminSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = serializer.data
        return Response({
            'data': response_data,
            'message': 'account created successfuly',
            'success': True 
            }, status=201)
