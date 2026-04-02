from django.db import models


class FacultyMember(models.Model):
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    instrument_tag = models.CharField(
        max_length=60,
        help_text="Space-separated tags for search filtering, e.g. 'piano voice'",
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
