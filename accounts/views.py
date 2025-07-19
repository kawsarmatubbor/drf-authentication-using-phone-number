from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .models import CustomUser

class RegistrationSerializer(serializers.ModelSerializer):
    password_2 = serializers.CharField(
        write_only = True,
        required = True
    )
    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'first_name', 'last_name', 'address', 'password', 'password_2']
        extra_kwargs = {
            'password' : {'write_only' : True},
            'address' : {'required': False}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            phone_number = validated_data['phone_number'],
            first_name = validated_data.get('first_name', ''),
            last_name = validated_data.get('last_name', ''),
            address = validated_data.get('address', ''),
            password = validated_data['password']
        )
        return user

class RegistrationView(APIView):
    def get(self, request):
        return Response("Registration(GET)")
    
    def post(self, request):
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Registration successful")
        return Response(serializer.errors)
    
class LoginView(APIView):
    def get(self, request):
        return Response("Login(GET)")
    
    def post(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        user = authenticate(phone_number = phone_number, password = password)

        if user is not None:
            login(request, user)
            return Response("Login successful")
        else:
            return Response("Something went wrong")
from rest_framework.decorators import api_view

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response("Logout successful")