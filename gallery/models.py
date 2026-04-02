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
    youtube_url = models.TextField(
        help_text=(
            "Paste the YouTube embed code (<iframe ...>) from Share → Embed, "
            "or a plain YouTube URL (youtu.be/... or youtube.com/watch?v=...)."
        ),
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
    def embed_src(self) -> str:
        """Return the bare src URL to use inside our own iframe."""
        raw = (self.youtube_url or "").strip()
        # Full <iframe> embed code — extract the src attribute
        m = re.search(r'src=["\']([^"\']+)["\']', raw)
        if m:
            return m.group(1)
        # Already an embed URL
        if "youtube.com/embed/" in raw:
            return raw
        # youtu.be/VIDEO_ID(?si=...)
        m = re.search(r"youtu\.be/([A-Za-z0-9_-]{11}([?][^\s]*)?)", raw)
        if m:
            path = m.group(1)
            vid = path[:11]
            qs = path[11:] if len(path) > 11 else ""
            return f"https://www.youtube.com/embed/{vid}{qs}"
        # youtube.com/watch?v=VIDEO_ID
        m = re.search(r"[?&]v=([A-Za-z0-9_-]{11})", raw)
        if m:
            # Preserve any extra query params (like si=)
            from urllib.parse import urlparse, parse_qs, urlencode
            parsed = urlparse(raw)
            qs = parse_qs(parsed.query)
            vid = m.group(1)
            keep = {k: v[0] for k, v in qs.items() if k != "v"}
            suffix = ("?" + urlencode(keep)) if keep else ""
            return f"https://www.youtube.com/embed/{vid}{suffix}"
        return raw
