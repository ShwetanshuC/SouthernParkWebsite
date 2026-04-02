from __future__ import annotations
from .models import SiteSettings, HeroSlide


def site_settings(request):
    settings_obj = SiteSettings.objects.first()
    if settings_obj is None:
        settings_obj = SiteSettings()
    hero_slides = HeroSlide.objects.filter(is_active=True).order_by("sort_order")
    return {"site_settings": settings_obj, "hero_slides": hero_slides}
