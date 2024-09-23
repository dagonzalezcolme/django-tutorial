from django.contrib import admin
from django.urls import path, include
from django.com import settings
from django.cof.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls')),
]

urlpatterns += staic(seetings.MEDIA_URL, document_root=settings.MEDIA_ROOT)