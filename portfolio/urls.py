from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("owner/", admin.site.urls),
    path("", include("web.urls", namespace="web")),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = "PORTFOLIO Administration"
admin.site.site_title = "PORTFOLIO Admin Portal"
admin.site.index_title = "Welcome to PORTFOLIO Admin Portal"