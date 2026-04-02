from django.shortcuts import render
from .models import PolicySection


def policies_view(request):
    sections = PolicySection.objects.filter(is_active=True)
    return render(request, "policies/policies.html", {"sections": sections})
