from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.
class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
