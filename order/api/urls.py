from django.urls import path
from .views import OrderListView, OrderDetailView

urlpatterns = [
    path('list-create', OrderListView.as_view(), name='order-list'),
    path('update-delete/<int:pk>', OrderDetailView.as_view(), name='order-detail'),
]
