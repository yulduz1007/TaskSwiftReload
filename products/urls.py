from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from products.views import ProductCreateAPIView, ProductListAPIView

urlpatterns = [
    path('product/create', ProductCreateAPIView.as_view()),
    path('product/get-all', ProductListAPIView.as_view()),
]