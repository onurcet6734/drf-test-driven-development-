from rest_framework import generics
from order.models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated

class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return Order.objects.filter(user = self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(user = self.request.user)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
