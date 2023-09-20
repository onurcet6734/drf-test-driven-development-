from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/menus/', include('menu.api.urls')),
    path('api/categories/', include('category.api.urls')),
    path('api/customers/', include('customer.api.urls')),
    path('api/orders/', include('order.api.urls')),
] 

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)