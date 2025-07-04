from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from orders.models import Order
from orders.serializer import OrderSerializer, OrderListSerializer
from users.permission import AdminPermission


# Create your views here.
class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OrderListAPIView(ListAPIView):
    """Phone number and name are not included, since all user data is collected from the authenticated user.
     To order a product, the user just needs to be logged in.
    """
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated, AdminPermission]
