from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import DieselData
from .serializers import DieselDataSerializer, UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    """user registration view """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            """create token for user """
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DieselDataList(generics.ListCreateAPIView):
    """list all diesel data"""
    queryset = DieselData.objects.all()
    serializer_class = DieselDataSerializer
    permission_classes = [permissions.IsAuthenticated]

class DieselDataDetail(generics.RetrieveUpdateDestroyAPIView):
    """retrieve, update, delete diesel data"""
    queryset = DieselData.objects.all()
    serializer_class = DieselDataSerializer
    permission_classes = [permissions.IsAuthenticated]
