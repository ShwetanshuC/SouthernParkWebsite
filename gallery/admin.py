from django.contrib import admin
from .models import GalleryPhoto, GalleryVideo


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ["caption", "sort_order", "is_active"]
    list_editable = ["sort_order", "is_active"]


@admin.register(GalleryVideo)
class GalleryVideoAdmin(admin.ModelAdmin):
    list_display = ["title", "youtube_url", "sort_order", "is_active"]
    list_editable = ["sort_order", "is_active"]
