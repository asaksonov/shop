from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("", include('catalog.urls', namespace='catalog')),
                  path("backoffice/", include('backoffice.urls', namespace='backoffice')),
                  path("blog/", include('blog.urls', namespace='blog'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
