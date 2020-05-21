from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from land.views import login_view

urlpatterns = [
    path('', include('land.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', login_view, name="shopix_login"),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
