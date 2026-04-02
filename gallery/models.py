import re
from django.db import models


class GalleryPhoto(models.Model):
    image = models.ImageField(upload_to="gallery/")
    caption = models.CharField(max_length=200, blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Gallery Photo"
        verbose_name_plural = "Gallery Photos"

    def __str__(self) -> str:
        return self.caption or f"Photo {self.id}"


class GalleryVideo(models.Model):
    title = models.CharField(max_length=200)
    youtube_url = models.URLField(
        max_length=500,
        help_text="Paste a YouTube link: https://youtu.be/... or https://www.youtube.com/watch?v=...",
    )
    caption = models.CharField(max_length=300, blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Gallery Video"
        verbose_name_plural = "Gallery Videos"

    def __str__(self) -> str:
        return self.title

    @property
    def embed_url(self) -> str:
        url = self.youtube_url.strip()
        # Already an embed URL
        if "youtube.com/embed/" in url:
            return url
        # youtu.be/VIDEO_ID
        m = re.search(r"youtu\.be/([A-Za-z0-9_-]{11})", url)
        if m:
            return f"https://www.youtube.com/embed/{m.group(1)}"
        # youtube.com/watch?v=VIDEO_ID
        m = re.search(r"[?&]v=([A-Za-z0-9_-]{11})", url)
        if m:
            return f"https://www.youtube.com/embed/{m.group(1)}"
        return url
