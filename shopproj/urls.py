from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from land.views import login_view

urlpatterns = [
    path('', include('land.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accoutns/login/', login_view, name="shopix_login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
