from django.urls import path
from . import  views

urlpatterns = [
  path('menu-items', views.MenuItemView.as_view(), name='menu-items'),
  path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),
  # path('booking', views.BookingViewSet.as_view(), name='booking'),
  path('users', views.UserView.as_view(), name='users'),
  path('users/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
]