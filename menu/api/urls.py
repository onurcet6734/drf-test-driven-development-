from django.urls import path
from .views import MenuItemListView, MenuItemDetailView

app_name = "menu"

urlpatterns = [
    path('list-create', MenuItemListView.as_view(), name='menuitem-list'),
    path('update-delete/<int:pk>', MenuItemDetailView.as_view(), name='menuitem-detail'),
]
