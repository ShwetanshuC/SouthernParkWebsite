from django.contrib import admin
from .models import FacultyMember


@admin.register(FacultyMember)
class FacultyMemberAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "sort_order", "is_active"]
    list_editable = ["sort_order", "is_active"]
