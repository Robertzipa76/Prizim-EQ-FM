from django.contrib import admin
from django.urls import path include , re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/(?P<version>(v1|v2))/', include('music.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #tgis helps in accessing media with native elements

