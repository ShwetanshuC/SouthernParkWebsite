from django.shortcuts import render
from .models import FacultyMember

CATEGORIES = [
    ("Piano",                 lambda t: "piano" in t),
    ("Violin & Viola",        lambda t: "violin" in t or "viola" in t),
    ("Cello",                 lambda t: "cello" in t),
    ("Flute & Oboe",          lambda t: "flute" in t or "oboe" in t),
    ("Saxophone & Clarinet",  lambda t: "saxophone" in t or "clarinet" in t),
    ("Voice",                 lambda t: "voice" in t and "piano" not in t),
    ("Staff",                 lambda t: "administrator" in t),
]


def faculty_list(request):
    members = list(FacultyMember.objects.filter(is_active=True).order_by("sort_order", "name"))
    groups = []
    assigned = set()
    for label, match in CATEGORIES:
        group = [m for m in members if m.pk not in assigned and match(m.instrument_tag.lower())]
        if group:
            for m in group:
                assigned.add(m.pk)
            groups.append((label, group))
    # Catch any unmatched members
    leftover = [m for m in members if m.pk not in assigned]
    if leftover:
        groups.append(("Other", leftover))
    return render(request, "faculty/faculty.html", {"faculty_groups": groups})
