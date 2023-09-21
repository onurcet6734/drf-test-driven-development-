from django.urls import path
from .views import MenuItemListView, MenuItemDetailView

urlpatterns = [
    path('list-create', MenuItemListView.as_view(), name='menuitem-list'),
    path('update-delete/<int:pk>', MenuItemDetailView.as_view(), name='menuitem-detail'),
]
