from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from orders.views import OrderCreateAPIView, OrderListAPIView

urlpatterns = [
    path('order/create', OrderCreateAPIView.as_view()),
    path('order/list', OrderListAPIView.as_view()),
]
