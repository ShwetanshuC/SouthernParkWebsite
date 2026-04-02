from django.contrib import admin
from .models import PolicySection


@admin.register(PolicySection)
class PolicySectionAdmin(admin.ModelAdmin):
    list_display = ["title", "sort_order", "is_active"]
    list_editable = ["sort_order", "is_active"]
