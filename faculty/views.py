from django.shortcuts import render
from .models import FacultyMember


def faculty_list(request):
    members = FacultyMember.objects.filter(is_active=True).order_by("sort_order", "name")
    return render(request, "faculty/faculty.html", {"faculty_members": members})
