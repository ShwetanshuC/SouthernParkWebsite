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
    readonly_fields = ["embed_src"]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["youtube_url"].help_text = (
            "Paste the full embed code from YouTube Share → Embed (<iframe ...>), "
            "or a plain link (youtu.be/... or youtube.com/watch?v=...). "
            "Using the embed code is recommended as it includes all required parameters."
        )
        return form
