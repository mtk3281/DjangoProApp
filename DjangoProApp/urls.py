from django.contrib import admin, auth
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/", include("accounts.urls")),
    path('', include('pages.urls')),
]+ static(
settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
