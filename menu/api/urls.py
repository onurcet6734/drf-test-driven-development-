from django.urls import path
from .views import MenuItemListView, MenuItemDetailView

urlpatterns = [
    path('', MenuItemListView.as_view(), name='menuitem-list'),
    path('<int:pk>', MenuItemDetailView.as_view(), name='menuitem-detail'),
]
