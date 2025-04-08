from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics, filters 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required.'})

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'})

        try:
            validate_password(password)
        except DjangoValidationError as e:
            raise ValidationError({'password': e.messages})

        user = User.objects.create_user(username=username, password=password)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'message': 'User registered successfully.',
         
        })


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required.'})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'message': f'Login successful. Hello {user.username}!'
            })

        return Response({'error': 'Invalid credentials'})



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            logout(request)
            
            return Response({'message': 'Logged out successfully.'})
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token or already logged out.'})



class TaskCreate(generics.ListCreateAPIView):
    
    permission_classes = [IsAuthenticated]
    
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'priority', 'status']
    
    ordering_fields = ['due_date', 'priority', 'status']


class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsAuthenticated]    
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

