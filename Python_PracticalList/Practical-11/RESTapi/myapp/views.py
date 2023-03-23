from rest_framework import generics
from myapp.models import User
from myapp.serializers import UserSerializer

class Userdata(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Userdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
