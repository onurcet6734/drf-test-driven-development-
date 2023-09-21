from django.urls import path
from .views import CategoryListView, CategoryDetailView

urlpatterns = [
    path('list-create', CategoryListView.as_view(), name='category-list'),
    path('update-delete/<slug>', CategoryDetailView.as_view(), name='category-detail'),
]
