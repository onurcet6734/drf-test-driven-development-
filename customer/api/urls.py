from django.urls import path
from .views import CustomerListView, CustomerDetailView

app_name = "customer"

urlpatterns = [
    path('list-create', CustomerListView.as_view(), name='customer-list'),
    path('update-delete/<int:pk>', CustomerDetailView.as_view(), name='customer-detail'),
]
