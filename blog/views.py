from django.shortcuts import render
from django.contrib.auth import get_user_model
from blog.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


User = get_user_model()
# Create your views here.

class Create_User(generics.CreateAPIView):
    """
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

