from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer


class UserCreate(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return Response({'info': 'You are already authenticated'})
        else:
            required_fields = ['username', 'password', 'first_name', 'last_name', 'email']
            return Response({'info': f'All registration fields are required: {required_fields}'})

    @swagger_auto_schema(request_body = UserSerializer, responses = {200: 'OK'})
    def post(self, request):
        """
        Create a new user.
        ---
        parameters:
          - name: username
            description: Username of the user
            required: true
            type: string
          - name: password
            description: Password of the user
            required: true
            type: string
          - name: first_name
            description: First name of the user
            required: true
            type: string
          - name: last_name
            description: Last name of the user
            required: true
            type: string
          - name: email
            description: Email of the user
            required: true
            type: string
        """
        required_fields = ['username', 'password', 'first_name', 'last_name', 'email']

        required_fields_str = ", ".join(required_fields)

        if any(field not in request.data for field in required_fields):
            return Response({'error': f'Missing required fields: {required_fields_str}'},
                            status = status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
