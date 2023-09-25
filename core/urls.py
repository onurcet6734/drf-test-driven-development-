from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/menus/', include('menu.api.urls',namespace='menu')),
    path('api/categories/', include('category.api.urls',namespace='category')),
    path('api/customers/', include('customer.api.urls',namespace='customer')),
    path('api/orders/', include('order.api.urls',namespace='order')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
] 

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)