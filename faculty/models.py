from django.db import models

INSTRUMENT_CHOICES = [
    ("piano",               "Piano"),
    ("piano voice",         "Piano & Voice"),
    ("violin viola",        "Violin & Viola"),
    ("violin",              "Violin"),
    ("viola",               "Viola"),
    ("cello",               "Cello"),
    ("flute",               "Flute"),
    ("oboe flute",          "Oboe & Flute"),
    ("oboe",                "Oboe"),
    ("saxophone clarinet",  "Saxophone & Clarinet"),
    ("saxophone",           "Saxophone"),
    ("clarinet",            "Clarinet"),
    ("voice",               "Voice"),
    ("guitar",              "Guitar"),
    ("drums",               "Drums / Percussion"),
    ("administrator",       "Staff / Administrator"),
]


class FacultyMember(models.Model):
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    instrument_tag = models.CharField(
        max_length=60,
        choices=INSTRUMENT_CHOICES,
        help_text="Primary instrument category for grouping and search filtering.",
    )
    photo = models.ImageField(upload_to="faculty/", blank=True, null=True)
    bio = models.TextField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "name"]
        verbose_name = "Faculty Member"
        verbose_name_plural = "Faculty Members"

    def __str__(self) -> str:
        return self.name
