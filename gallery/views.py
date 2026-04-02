from django.shortcuts import render
from .models import GalleryPhoto


def gallery_view(request):
    photos = GalleryPhoto.objects.filter(is_active=True)
    return render(request, "gallery/gallery.html", {"photos": photos})
