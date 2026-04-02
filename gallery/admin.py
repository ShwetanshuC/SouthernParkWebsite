from django.contrib import admin
from .models import GalleryPhoto


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ["caption", "sort_order", "is_active"]
    list_editable = ["sort_order", "is_active"]
