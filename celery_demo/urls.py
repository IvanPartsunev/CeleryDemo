from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("celery_demo.project_core.urls")),
    path("beat/", include("celery_demo.celery_beat.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
