from django.shortcuts import render
from django.contrib.auth.models import User
from .models import MenuItem, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework import permissions



class UserView(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def list(self, request, *args, **kwargs):
      queryset = self.filter_queryset(self.get_queryset())
      serializer = self.get_serializer(queryset, many=True, context={'request': request})
      return Response(serializer.data)

  def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data, context={'request': request})
      serializer.is_valid(raise_exception=True)
      self.perform_create(serializer)
      headers = self.get_success_headers(serializer.data)
      return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED, headers=headers)



class UserDetailView(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer



class BookingViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticated]
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
    
    

class MenuItemView(generics.ListCreateAPIView):
  permission_classes = [permissions.IsAuthenticated]
  queryset = MenuItem.objects.all()
  serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  permission_classes = [permissions.IsAuthenticated]
  queryset = MenuItem.objects.all()
  serializer_class = MenuSerializer