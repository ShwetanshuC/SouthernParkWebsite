from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Southern Park Music School Admin"
admin.site.site_title = "SPMS Admin"
admin.site.index_title = "Site administration"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("faculty/", include("faculty.urls")),
    path("gallery/", include("gallery.urls")),
    path("policies/", include("policies.urls")),
    path("", include("pages.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
